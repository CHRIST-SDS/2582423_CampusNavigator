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
