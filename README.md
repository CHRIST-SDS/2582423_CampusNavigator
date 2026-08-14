# 🧭 CHRIST University Smart Campus Navigator

An **AI-powered campus navigation assistant** designed to help students, faculty, and visitors find locations across the **CHRIST University Central Campus, Bengaluru** using natural-language queries.

The system combines **Natural Language Processing (NLP)**, **semantic similarity**, and a lightweight **Transformer-based language model** to understand user queries, identify the appropriate campus location, handle ambiguous requests, and provide a natural-language navigation response.

---

## 📌 Problem Statement

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

---

## ✨ Features

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