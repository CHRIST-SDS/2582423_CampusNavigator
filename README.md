# 🧭 Campus Navigator

## 🤖 GenAI-Powered Smart Campus Navigation Assistant

> An intelligent campus navigation assistant designed to help students and visitors find departments, offices, libraries, food facilities, sports facilities, academic buildings, and other important locations across the **CHRIST University Central Campus, Bengaluru**.

---

## 📌 Problem Statement

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

---

## ✨ Features

### 🤖 Natural Language Campus Search

Users can search for campus locations using normal conversational questions instead of exact location names.

Examples:

- *"Where can I study?"*
- *"Where do I go for placements?"*
- *"Where can I get food?"*
- *"How do I reach the MCA department?"*
- *"Where can I play basketball?"*

---

### 🧠 Semantic Search

The system uses **Sentence Transformers** to convert user queries and campus locations into semantic embeddings.

This allows the system to identify locations based on meaning rather than relying only on exact keyword matching.

**Example:**

```text
User Query
    ↓
"Where can I borrow books?"
    ↓
Semantic Matching
    ↓
📚 Central Library
