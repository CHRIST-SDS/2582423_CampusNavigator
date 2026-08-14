# 🏫 GenAI Powered Smart Campus Navigation Assistant

> 🤖 An AI-powered conversational campus navigation assistant for CHRIST University Central Campus, Bengaluru.

The **GenAI Powered Smart Campus Navigation Assistant** helps students, faculty, staff, and visitors find departments, offices, libraries, food facilities, sports facilities, academic buildings, and other important campus locations using natural-language queries.

---

# 📌 Problem Statement

Large university campuses contain multiple academic buildings, departments, administrative offices, libraries, food facilities, sports areas, and other facilities.

Students and visitors may face difficulties in:

- 📍 Finding the correct campus location
- 🏢 Identifying the building containing a particular facility
- 🏬 Finding the correct floor or block
- 📚 Identifying the correct library when multiple libraries exist
- 🍴 Finding food facilities
- 🏀 Finding sports facilities
- 🧑‍💼 Locating administrative and placement offices
- 🗺️ Understanding how to reach a destination
- ❓ Asking navigation questions without knowing the exact location name

Traditional campus navigation systems often depend on static maps or manually searching for locations.

Therefore, this project develops an **AI-powered conversational navigation assistant** that understands natural-language questions, identifies the appropriate campus location, handles ambiguous queries, and provides verified location and route information in a natural conversational format.

---

# 🎯 Objectives

The main objectives of the project are:

- 🧠 Understand natural-language campus queries
- 🔎 Identify the most relevant campus location
- 📍 Perform semantic location matching
- ❓ Detect ambiguous queries involving multiple locations
- 💬 Ask clarification questions when required
- 🏢 Provide building and floor information
- 🗺️ Provide route guidance
- 🤖 Generate natural-language responses using a Transformer model
- ⚡ Provide an interactive chatbot interface
- 🔒 Keep campus information based on verified campus data
- 🖥️ Support local execution without requiring a paid external AI API

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

# 🏗️ Architecture Diagram

The overall architecture of the system is:

```text
                         👤 USER
                           │
                           │ Natural Language Query
                           ▼
                 ┌──────────────────────┐
                 │    React Frontend    │
                 │   Chatbot Interface  │
                 └──────────┬───────────┘
                            │
                            │ HTTP POST /chat
                            ▼
                 ┌──────────────────────┐
                 │    Flask Backend     │
                 │      REST API        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Query Processing   │
                 │ Text Normalization   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Sentence Transformer │
                 │  all-MiniLM-L6-v2    │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Semantic Similarity  │
                 │   Location Matching  │
                 └──────────┬───────────┘
                            │
                ┌───────────┴────────────┐
                │                        │
                ▼                        ▼
       ┌────────────────┐       ┌──────────────────┐
       │ Single Match   │       │ Multiple Matches │
       └───────┬────────┘       └────────┬─────────┘
               │                         │
               │                         ▼
               │                ┌──────────────────┐
               │                │  Clarification   │
               │                │     Question     │
               │                └────────┬─────────┘
               │                         │
               └────────────┬────────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Verified Campus Data │
                 │   campus_data.json   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    FLAN-T5 Small     │
                 │ Natural Language Gen │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │   Final AI Response  │
                 │ Location + Route     │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │    React Chat UI     │
                 └──────────────────────┘
```

---

# 🔄 System Workflow

The complete workflow of the application is:

```text
User enters a question
          ↓
Frontend sends query to Flask API
          ↓
Backend receives the query
          ↓
Text normalization
          ↓
Semantic embedding generation
          ↓
Compare query with campus locations
          ↓
Identify relevant location
          ↓
Check for ambiguity
          ↓
 ┌─────────────────────────────┐
 │ Multiple locations detected?│
 └──────────────┬──────────────┘
                │
          YES   │   NO
           ↓    │    ↓
    Ask clarification
           │         │
           └────┬────┘
                ↓
      Retrieve verified data
                ↓
       Generate AI response
                ↓
        Add route information
                ↓
       Return JSON response
                ↓
        Display in chatbot
```

---

# 🧠 NLP Pipeline

The Natural Language Processing pipeline consists of the following stages:

## 1️⃣ Query Input

The user enters a natural-language query.

Example:

```text
Where can I borrow books?
```

---

## 2️⃣ Text Normalization

The query is converted into a normalized representation.

Example:

```text
Where Can I Borrow Books?
```

becomes:

```text
where can i borrow books
```

This improves consistency during matching.

---

## 3️⃣ Semantic Embedding

The normalized query is converted into a vector representation using:

```text
all-MiniLM-L6-v2
```

Campus locations are also converted into vector representations.

---

## 4️⃣ Similarity Calculation

Cosine similarity is used to compare the query embedding against campus location embeddings.

```text
User Query
    ↓
Embedding
    ↓
Cosine Similarity
    ↓
Campus Location Ranking
```

The location with the strongest semantic match is selected.

---

## 5️⃣ Ambiguity Detection

The system checks whether multiple locations could satisfy the query.

Example:

```text
Where is the library?
```

If multiple libraries exist, the system asks the user to clarify.

---

## 6️⃣ Verified Information Retrieval

Once the destination is identified, the system retrieves information from:

```text
campus_data.json
```

This contains information such as:

- Location name
- Category
- Building
- Floor
- Description
- Keywords
- Route

---

## 7️⃣ Natural Language Generation

The verified information is passed to:

```text
Google FLAN-T5 Small
```

The model generates a natural conversational response.

---

## 8️⃣ Final Response

The backend returns the final response to the React frontend.

The frontend displays the response in the chatbot interface.

---

# 🤖 AI Models Used

## Sentence Transformer

### Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Purpose

Used for:

- Semantic search
- Query representation
- Location matching
- Similarity calculation

---

## FLAN-T5

### Model

```text
google/flan-t5-small
```

### Purpose

Used for:

- Natural-language response generation
- Converting verified campus information into conversational responses
- Improving the chatbot interaction experience

---

# 🗃️ Campus Data

Campus information is stored in:

```text
backend/campus_data.json
```

---

# 🧩 Technology Stack

| Layer | Technology |
|---|---|
| 🎨 Frontend | React.js |
| ⚡ Build Tool | Vite |
| 🎨 UI Icons | Lucide React |
| 🔙 Backend | Flask |
| 🌐 API | Flask REST API |
| 🧠 NLP | Sentence Transformers |
| 🔎 Embedding Model | all-MiniLM-L6-v2 |
| 🤖 Generative AI | Google FLAN-T5 Small |
| 🧮 Deep Learning Framework | PyTorch |
| 📊 Similarity Metric | Cosine Similarity |
| 💾 Data Storage | JSON |
| 🔗 Communication | HTTP / REST API |
| 🐙 Version Control | Git |
| ☁️ Repository | GitHub |

---

# 📁 Project Structure

```text
CampusNavigator/
│
├── backend/
│   ├── app.py
│   ├── chatbot.py
│   ├── campus_data.json
│   ├── requirements.txt
│   └── venv/
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── data/
│
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation

## 📋 Prerequisites

Install the following before running the project:

- 🐍 Python 3.10 or higher
- 🟢 Node.js
- 📦 npm
- 🐙 Git
- 💻 Visual Studio Code

---

# 🔙 Backend Setup

Open a terminal and navigate to the backend:

```bash
cd CampusNavigator/backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install flask flask-cors torch transformers sentence-transformers
```

Alternatively:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Backend

Start the Flask server:

```bash
python app.py
```

The backend should start at:

```text
http://127.0.0.1:5000
```

The terminal should display something similar to:

```text
CHRIST UNIVERSITY SMART CAMPUS NAVIGATOR
Flask API starting...
Debugger is active!
```

---

# 🎨 Frontend Setup

Open a second terminal.

Navigate to the frontend:

```bash
cd CampusNavigator/frontend
```

Install the required Node packages:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend should be available at:

```text
http://localhost:5173
```

---

# 🚀 Application Usage

## Step 1️⃣

Start the backend:

```bash
cd backend
venv\Scripts\activate
python app.py
```

---

## Step 2️⃣

Open another terminal and start the frontend:

```bash
cd frontend
npm run dev
```

---

## Step 3️⃣

Open the application in the browser:

```text
http://localhost:5173
```

---

## Step 4️⃣

Enter a natural-language query.

Example:

```text
Where can I borrow books?
```

---

## Step 5️⃣

The system identifies the relevant location and provides:

- 📍 Destination
- 🏢 Building
- 🪜 Floor
- 🤖 Natural-language explanation
- 🗺️ Route


---

# 📸 Screenshots

## 🖥️ 1. Main Chatbot Interface

The main interface displays the AI-powered campus navigation chatbot.

**Screenshot:**

> 📷 Add screenshot here.

<br>

---

## 💬 2. Natural Language Query

The user enters a natural-language campus query.

**Example:**

```text
Where can I borrow books?
```

**Screenshot:**

> 📷 Add screenshot here.

<br>

---

## 🤖 3. AI Response

The assistant generates a natural-language response containing the relevant campus information.

**Screenshot:**

> 📷 Add screenshot here.

<br>

---

## ❓ 4. Clarification Response

When multiple locations match the query, the chatbot asks the user to select the appropriate location.

**Screenshot:**

> 📷 Add screenshot here.

<br>

---

## 🏢 5. Building and Floor Information

The system displays the building and floor associated with the selected campus location.

**Screenshot:**

> 📷 Add screenshot here.

<br>

---

## 🗺️ 6. Route Guidance

The chatbot provides route guidance from the campus entrance to the selected destination.

**Screenshot:**

> 📷 Add screenshot here.

<br>

---

# 🎥 Demo Video

A complete demonstration of the project can be added here.

**Demo Video:**

> 🎬 Add your project demonstration video link here.

Example:

```text
[▶️ Watch Project Demo](YOUR_VIDEO_LINK_HERE)
```

---

# 🔮 Future Enhancements

The current system can be extended with:

- 🗺️ Interactive campus map integration
- 📍 GPS-based navigation
- 🧭 Turn-by-turn navigation
- 🚶 Walking distance estimation
- 🏢 Real-time building availability
- 🕐 Facility opening and closing times
- 📅 Event-based navigation
- 🎤 Voice-based queries
- 🔊 Voice responses
- 🌐 Multilingual campus assistance
- 📱 Mobile application
- 🧠 Larger and more capable local LLM
- 🗺️ Map-based route visualization
- 📍 User's current-location detection
- 🔄 Dynamic campus information updates
- 👨‍🎓 Personalized student navigation
- ♿ Accessibility-aware routes

---

# 🚧 Current Limitations

The current prototype has some limitations:

- Campus information depends on the accuracy of `campus_data.json`.
- Route guidance is based on predefined campus routes.
- GPS-based navigation is not currently implemented.
- Real-time campus changes are not automatically detected.
- FLAN-T5 Small has limited generative capabilities compared with larger LLMs.
- The current system is primarily designed for the CHRIST University Central Campus.

---

# 📜 License

This project is developed for academic and educational purposes.

---

# 🙏 Acknowledgements

This project makes use of open-source technologies and models including:

- 🤗 Hugging Face Transformers
- 🤗 Sentence Transformers
- 🔥 PyTorch
- 🌐 Flask
- ⚛️ React
- ⚡ Vite
- 🎨 Lucide React

---

# ⭐ If You Find This Project Useful

If you find this project interesting, consider giving the repository a ⭐ on GitHub!

```text
🏫 Smart Campus
        +
🧠 NLP
        +
🤖 Generative AI
        +
💬 Conversational Interface
        =
🚀 Intelligent Campus Navigation
```
