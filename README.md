<<<<<<< HEAD
# 🧭 CHRIST University Smart Campus Navigator

An **AI-powered campus navigation assistant** designed to help students, faculty, and visitors find locations across the **CHRIST University Central Campus, Bengaluru** using natural-language queries.

The system combines **Natural Language Processing (NLP)**, **semantic similarity**, and a lightweight **Transformer-based language model** to understand user queries, identify the appropriate campus location, handle ambiguous requests, and provide a natural-language navigation response.
=======
# 🧭 Campus Navigator

## 🤖 GenAI-Powered Smart Campus Navigation Assistant

> An intelligent campus navigation assistant designed to help students and visitors find departments, offices, libraries, food facilities, sports facilities, academic buildings, and other important locations across the **CHRIST University Central Campus, Bengaluru**.
>>>>>>> 831127fa39ba21e562154e86b923c395ef34a65a

---

## 📌 Problem Statement

<<<<<<< HEAD
Large university campuses contain numerous:

- 🏫 Academic buildings
- 📚 Libraries
- 🍴 Food facilities
- 🏢 Administrative offices
- 🎓 Academic departments
- 🏀 Sports facilities
- 🚪 Campus entrances
- 🧑‍💼 Placement and career offices
- 🧑‍🔬 Laboratories
- 🛋️ Student facilities
- 📍 Other important landmarks

For new students, visitors, and even existing students, finding the correct location can be difficult, especially when multiple facilities belong to the same category.

For example, a user may ask:

> **"Where can I study?"**

or

> **"Where can I eat?"**

Instead of forcing users to search through a fixed list of locations, the proposed system allows users to communicate naturally with the campus assistant.

The system:

1. 🧠 Understands the user's natural-language query.
2. 🔎 Identifies the most relevant campus location.
3. 🤔 Detects ambiguity when multiple locations may match.
4. 💬 Asks the user for clarification when necessary.
5. 📍 Provides the selected location's building and floor.
6. 🛣️ Generates a natural-language route.
7. 🤖 Uses a Transformer model to produce human-readable responses.
=======
Large university campuses contain numerous academic buildings, departments, administrative offices, libraries, food facilities, sports areas, and student services.

Finding the correct location can be difficult because:

- 🏫 Multiple buildings provide similar services.
- 📚 Multiple libraries and study facilities may exist.
- 🍽️ Multiple food facilities may be available.
- 🏀 Multiple sports facilities are distributed across the campus.
- 🏢 Departments and offices are located across different buildings and floors.
- 🧭 Traditional campus maps require users to manually identify locations.
- 💬 Students usually ask questions using natural language instead of exact location names.

### 🎯 Proposed Solution

**Campus Navigator** is a conversational AI-based navigation system that allows users to ask questions in natural language.

For example:

> 💬 *"Where can I borrow books?"*

> 💬 *"Where is the MCA department?"*

> 💬 *"Where can I eat?"*

> 💬 *"Where do I go for campus placements?"*

> 💬 *"Where is the basketball court?"*

The system understands the user's query, identifies the most relevant campus location, handles ambiguity when multiple locations match, and provides a natural-language response with verified location and route information.
>>>>>>> 831127fa39ba21e562154e86b923c395ef34a65a

---

## ✨ Features

<<<<<<< HEAD
### 🤖 Natural Language Campus Assistant

Users can ask questions naturally instead of selecting locations from menus.

Example:

```text
Where can I borrow books?

🧠 Semantic Search

The system uses:

Sentence Transformers (all-MiniLM-L6-v2)

to convert:

User queries
Campus locations
Keywords
Descriptions

into numerical embeddings.

Cosine similarity is then used to identify the most relevant campus location.
=======
- 🤖 **Natural Language Interaction**  
  Users can ask campus-related questions using normal conversational language instead of selecting from predefined menus.

- 🧠 **Semantic Search**  
  Uses the `all-MiniLM-L6-v2` Sentence Transformer to understand the semantic meaning of user queries and match them with campus locations.

- 🔀 **Ambiguity Detection**  
  When multiple locations can match a query, the system identifies the ambiguity instead of selecting an incorrect location.

- 💬 **Intelligent Clarification**  
  The chatbot asks the user which specific location they mean when multiple possible destinations are found.

- 📍 **Location Identification**  
  Identifies the most relevant campus destination from the user's query.

- 🏢 **Building & Floor Information**  
  Provides the building and floor associated with the selected campus location.

- 🛣️ **Natural Language Route Guidance**  
  Provides a human-readable route to help users reach their selected destination.

- 🤖 **Transformer-Based Response Generation**  
  Uses **Google FLAN-T5 Small** to generate concise and natural-language responses from verified campus information.

- 📚 **Multiple Campus Facilities**  
  Supports academic departments, libraries, food facilities, administrative offices, placement offices, sports facilities, entrances, and other campus landmarks.

- 🗂️ **Structured Campus Knowledge Base**  
  Campus locations are maintained in a JSON-based knowledge base containing location names, categories, buildings, floors, descriptions, keywords, and routes.

- ⚡ **Lightweight Local AI**  
  Uses lightweight NLP and Transformer models that can run locally without requiring a large external LLM API.

---

## 🏗️ Architecture Diagram

```text
                    ┌───────────────────────┐
                    │         USER          │
                    │ Natural Language Query│
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │    React Frontend     │
                    │       + Vite          │
                    └───────────┬───────────┘
                                │
                         HTTP POST /chat
                                │
                                ▼
                    ┌───────────────────────┐
                    │    Flask Backend      │
                    │       REST API        │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Query Processing    │
                    │    & Normalization    │
                    └───────────┬───────────┘
                                │
                 ┌──────────────┴──────────────┐
                 │                             │
                 ▼                             ▼
      ┌─────────────────────┐      ┌─────────────────────┐
      │ Sentence Transformer│      │ Ambiguity Detection │
      │  all-MiniLM-L6-v2   │      │                     │
      └──────────┬──────────┘      └──────────┬──────────┘
                 │                             │
                 └──────────────┬──────────────┘
                                ▼
                    ┌───────────────────────┐
                    │ Campus Knowledge Base │
                    │   campus_data.json    │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ Location Identification│
                    │ Building + Floor      │
                    │ Description + Route   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     FLAN-T5 Small     │
                    │ Natural Language      │
                    │ Response Generation   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   JSON API Response   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │    React Chat UI      │
                    │ Conversational Output │
                    └───────────────────────┘
>>>>>>> 831127fa39ba21e562154e86b923c395ef34a65a
