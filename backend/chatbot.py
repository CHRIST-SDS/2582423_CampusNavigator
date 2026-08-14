import json
import re
import os
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
import torch


# 1. LOAD SENTENCE TRANSFORMER
print("Loading Sentence Transformer...")
semantic_model = SentenceTransformer("all-MiniLM-L6-v2")
print("Sentence Transformer loaded.")

# 2. LOAD FLAN-T5
MODEL_NAME = "google/flan-t5-small"
print("Loading FLAN-T5 Small...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

print("FLAN-T5 Small loaded.")

# 3. LOAD CAMPUS DATA
pending_clarification = {}
print("Loading campus data...")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "campus_data.json")

with open(DATA_FILE, "r", encoding="utf-8") as file:
    campus_data = json.load(file)

location_names = list(campus_data.keys())

# 5. CREATE TEXT FOR SEMANTIC SEARCH
print("Creating campus embeddings...")

location_texts = []

for location_name, location_info in campus_data.items():
    keywords = location_info.get("keywords",[])
    keyword_text = " ".join(keywords)

    text = " ".join([location_name,location_info.get("category",""),
        location_info.get("building",""),
        location_info.get("description",""),
        keyword_text
    ])

    location_texts.append(text)

# 6. CREATE EMBEDDINGS
location_embeddings = semantic_model.encode(location_texts,convert_to_tensor=True)
print("Campus embeddings created.")

# 7. TEXT NORMALIZATION

def normalize_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]"," ",text)
    text = re.sub(r"\s+"," ",text)

    return text.strip()

# 8. FLAN-T5 RESPONSE GENERATION
def generate_ai_response(query, location_name, location_info):

    building = location_info.get("building", "Central Campus")
    floor = location_info.get("floor", "Ground Level")
    description = location_info.get("description", "")

    prompt = f"""
        Question: {query}
        Place: {location_name}
        Location: {building}
        Floor: {floor}
        Information: {description}

        Answer the question naturally in one sentence:
        """

    try:
        inputs = tokenizer(prompt,return_tensors="pt",truncation=True,max_length=256)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=30,
                num_beams=5,
                do_sample=False,
                no_repeat_ngram_size=3
            )

        response = tokenizer.decode(outputs[0],skip_special_tokens=True).strip()

        print("\n========== FLAN-T5 ==========")
        print("Question:", query)
        print("Generated:", response)
        print("=============================")

        return clean_ai_response(
            response,
            query,
            location_name,
            location_info
        )

    except Exception as e:

        print("FLAN-T5 error:", e)

        return fallback_response(
            query,
            location_name,
            location_info
        )

# CLEAN RESPONSE
def clean_ai_response(response, query, location_name, location_info):

    response = response.strip()

    bad_phrases = [
        "you are a friendly",
        "you are an ai",
        "answer the question",
        "question:",
        "place:",
        "location:",
        "floor:",
        "information:",
        "write",
        "no.",
        "1.",
        "2.",
        "3."
    ]

    lower_response = response.lower()

    for phrase in bad_phrases:
        if phrase in lower_response:
            print("Poor FLAN-T5 response detected.")
            return fallback_response(
                query,
                location_name,
                location_info
            )

    words = response.split()

    if len(words) < 5:
        return fallback_response(
            query,
            location_name,
            location_info
        )

    return response

# FALLBACK RESPONSE AS FLAN MODEL IS SMALL
def fallback_response(query, location_name, location_info):

    query_lower = query.lower()

    building = location_info.get(
        "building",
        "Central Campus"
    )
    description = location_info.get(
        "description",
        ""
    )
    if any(word in query_lower for word in [
        "eat", "food", "hungry", "lunch",
        "dinner", "snack", "drink"
    ]):

        return (
            f"If you're looking for something to eat, "
            f"you can head to the {location_name} in "
            f"{building}. {description}"
        )

    if any(word in query_lower for word in [
        "book", "books", "library",
        "borrow", "read", "study"
    ]):

        return (
            f"You can visit the {location_name} in "
            f"{building} to access books and study resources."
        )

    if any(word in query_lower for word in [
        "mca", "department", "faculty"
    ]):

        return (
            f"The {location_name} is located in {building}. "
            f"You can head there for the relevant academic services."
        )

    if any(word in query_lower for word in [
        "basketball", "sport", "play", "court"
    ]):

        return (
            f"If you'd like to play, head to the "
            f"{location_name} in {building}."
        )

    if any(word in query_lower for word in [
        "placement", "placements", "career", "job"
    ]):

        return (
            f"For campus placements, head to the "
            f"{location_name} in {building}."
        )

    return (
        f"You can find the {location_name} in "
        f"{building}. {description}"
    )

def build_location_response(query, location_name, location_info, confidence=None):
    category = location_info.get("category", "Campus Facility")
    building = location_info.get("building", "Central Campus")
    floor = location_info.get("floor", "Refer to current campus allocation")
    description = location_info.get("description", "")
    route = location_info.get("route", [])

    ai_response = generate_ai_response(query,location_name,location_info)

    result = {
        "success": True,
        "query": query,
        "destination": location_name,
        "category": category,
        "building": building,
        "floor": floor,
        "description": description,
        "response": ai_response,
        "route": route
    }

    if confidence is not None:
        result["confidence"] = round(confidence, 3)

    return result

# AMBIGUITY DETECTION
def find_ambiguous_locations(query):
    query_lower = normalize_text(query)

    category_terms = {
        "library": ["library", "libraries", "books", "reading room", "study room"],
        "Food Facility": ["food", "eat", "eating", "hungry", "canteen", "cafeteria", "snack", "restaurant"],
        "Sports": ["sports", "sport", "play", "game", "court", "basketball", "football", "cricket"],
        "Academic Department": ["department", "faculty", "mca", "bca", "bba", "computer science"],
        "Office": ["Office", "administratative", "admin"],
        "Placement": ["placement", "placements", "career", "recruitment"],
    }

    detected_category = None

    for category, terms in category_terms.items():
        if any(term in query_lower for term in terms):
            detected_category = category
            break

    if detected_category == "library":
        matches = []
        for name, info in campus_data.items():
            text = normalize_text(
                name + " " +
                info.get("category", "") + " " +
                info.get("description", "") + " " +
                " ".join(info.get("keywords", []))
            )

            if (
                "library" in text or
                "books" in text or
                "reading" in text
            ):
                matches.append({
                    "name": name,
                    "info": info
                })
        return matches

    if not detected_category:
        return []

    matches = []

    for name, info in campus_data.items():
        category = info.get("category", "")

        if category.lower() == detected_category.lower():
            matches.append({
                "name": name,
                "info": info
            })

    return matches

# semantic matches for better clarity and response for the llm
def find_semantic_matches(query, threshold=0.35):

    query_embedding = semantic_model.encode(
        query,
        convert_to_tensor=True
    )

    similarities = util.cos_sim(
        query_embedding,
        location_embeddings
    )[0]

    matches = []

    for i, score in enumerate(similarities):

        score = float(score)

        if score >= threshold:

            matches.append({
                "name": location_names[i],
                "info": campus_data[location_names[i]],
                "score": score
            })

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return matches

# CLARIFICATION RESPONSE FOR THEAMBIGUITY
def clarification_response(query, locations):

    global pending_clarification
    pending_clarification = {"options": locations}

    names = [
        location["name"]
        for location in locations
    ]

    if len(names) == 2:
        options = (f"{names[0]} or {names[1]}")
    else:
        options = (", ".join(names[:-1])+ " or "+ names[-1])

    return {
        "success": True,
        "clarification": True,
        "query": query,
        "response": (
            "I found a few places that could "
            f"match your request. Which one "
            f"are you looking for: {options}?"
        ),
        "options": names
    }

# PROCESS USER QUERY
def process_query(query):
    global pending_clarification
    query = query.strip()

    if not query:
        return {
            "success": False,
            "message": "Please enter a question."
        }

    query_lower = normalize_text(query)

    # Detect whether this is a completely new question
    new_question_terms = [
        "where", "what", "which", "how", "find", "locate",
        "where is", "where can", "how do i", "tell me"
    ]

    is_new_question = any(
        term in query_lower
        for term in new_question_terms
    )

    # Use clarification only when the message is an actual option
    if pending_clarification and not is_new_question:
        options = pending_clarification.get("options", [])

        for location in options:
            name = normalize_text(location["name"])

            if name in query_lower or query_lower in name:
                pending_clarification = {}

                return build_location_response(
                    query,
                    location["name"],
                    location["info"]
                )

    # Always clear old clarification for a new question
    if is_new_question:
        pending_clarification = {}

    # Check whether the current query has multiple possible locations
    ambiguous = find_ambiguous_locations(query)

    if len(ambiguous) > 1:
        return clarification_response(
            query,
            ambiguous
        )

    # If exactly one category-specific location exists, use it
    if len(ambiguous) == 1:
        location = ambiguous[0]

        return build_location_response(
            query,
            location["name"],
            location["info"]
        )

    # Fall back to semantic search for general campus queries
    query_embedding = semantic_model.encode(
        query,
        convert_to_tensor=True
    )

    similarities = util.cos_sim(
        query_embedding,
        location_embeddings
    )[0]

    best_index = int(similarities.argmax())
    confidence = float(similarities[best_index])

    location_name = location_names[best_index]
    location_info = campus_data[location_name]

    if confidence < 0.25:
        return {
            "success": False,
            "message": (
                "I could not confidently identify the campus location. "
                "Please try asking about a department, office, facility "
                "or landmark."
            ),
            "query": query,
            "confidence": round(confidence, 3)
        }

    return build_location_response(
        query,
        location_name,
        location_info,
        confidence
    )