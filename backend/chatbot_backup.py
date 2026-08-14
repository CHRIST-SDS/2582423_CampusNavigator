from sentence_transformers import SentenceTransformer, util

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from navigation import get_campus_data


# ============================================================
# 1. LOAD NLP MODEL
# ============================================================

print("Loading Sentence Transformer...", flush=True)

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

print("Sentence Transformer loaded.", flush=True)


# ============================================================
# 2. LOAD LLM
# ============================================================

print("Loading FLAN-T5 Small...", flush=True)

LLM_NAME = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(LLM_NAME)

llm_model = AutoModelForSeq2SeqLM.from_pretrained(
    LLM_NAME
)

print("FLAN-T5 Small loaded.", flush=True)


# ============================================================
# 3. LOAD CAMPUS KNOWLEDGE BASE
# ============================================================

campus_data = get_campus_data()

location_names = list(campus_data.keys())


# ============================================================
# 4. CREATE SEARCHABLE LOCATION TEXT
# ============================================================

location_texts = []

for location, data in campus_data.items():

    text = " ".join([
        location,
        data.get("category", ""),
        data.get("building", ""),
        data.get("floor", ""),
        data.get("description", ""),
        " ".join(data.get("keywords", []))
    ])

    location_texts.append(text)


print("Creating campus embeddings...", flush=True)

location_embeddings = embedding_model.encode(
    location_texts,
    convert_to_tensor=True
)

print("Campus embeddings created.", flush=True)


# ============================================================
# 5. FIND LOCATION
# ============================================================

def find_location(user_query):

    query_embedding = embedding_model.encode(
        user_query,
        convert_to_tensor=True
    )

    similarities = util.cos_sim(
        query_embedding,
        location_embeddings
    )[0]

    best_index = int(similarities.argmax())

    best_score = float(similarities[best_index])

    best_location = location_names[best_index]

    return best_location, best_score


# ============================================================
# 6. GENERATE RESPONSE USING FLAN-T5
# ============================================================

def generate_response(user_query, location_name):

    location = campus_data[location_name]

    route = location.get("route", [])

    route_text = " → ".join(route)

    prompt = f"""
You are a helpful university campus navigation assistant.

Answer the following user question.

User:
{user_query}

The correct destination is:
{location_name}

Category:
{location.get("category", "")}

Building:
{location.get("building", "")}

Floor:
{location.get("floor", "")}

Description:
{location.get("description", "")}

Navigation route:
{route_text}

Write a concise response in natural English.

Start by clearly telling the user the destination.
Then provide the available location information.
Then provide the route.

Do not invent any information.
Do not change the route.
"""

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    outputs = llm_model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=False
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    ).strip()

    # Safety fallback if FLAN-T5 produces a poor response
    if (
        len(response) < 30
        or response.lower() in ["route", "destination"]
    ):

        response = (
            f"The destination is {location_name}. "
            f"{location.get('description', '')} "
            f"The suggested route is: {route_text}."
        )

    return response


# ============================================================
# 7. MAIN CHATBOT FUNCTION
# ============================================================

def process_query(user_query):

    location_name, confidence = find_location(
        user_query
    )

    print(
        f"Matched location: {location_name} "
        f"(confidence={confidence:.3f})",
        flush=True
    )

    # Reject weak matches
    if confidence < 0.30:

        return {
            "success": False,
            "message": (
                "I could not confidently identify the "
                "campus location. Please try asking about "
                "a department, office, facility or landmark."
            )
        }

    location = campus_data[location_name]

    response = generate_response(
        user_query,
        location_name
    )

    return {

        "success": True,

        "query": user_query,

        "destination": location_name,

        "confidence": round(
            confidence,
            3
        ),

        "category": location.get(
            "category",
            ""
        ),

        "building": location.get(
            "building",
            ""
        ),

        "floor": location.get(
            "floor",
            ""
        ),

        "description": location.get(
            "description",
            ""
        ),

        "route": location.get(
            "route",
            []
        ),

        "response": response
    }