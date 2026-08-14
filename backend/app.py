from flask import Flask, request, jsonify
from flask_cors import CORS

from chatbot import process_query

app = Flask(__name__)

# Allow React frontend to communicate with Flask
CORS(app)


@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "status": "success",
        "message": "Christ University Smart Campus Navigator API is running"
    })


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json(silent=True)

        if not data or "query" not in data:
            return jsonify({
                "success": False,
                "message": "Please provide a query."
            }), 400

        user_query = str(data["query"]).strip()

        if not user_query:
            return jsonify({
                "success": False,
                "message": "Query cannot be empty."
            }), 400

        # Process query using Sentence Transformer + FLAN-T5
        result = process_query(user_query)

        # Make sure a valid response exists
        ai_response = result.get(
            "response",
            "I'm sorry, I couldn't find the information you are looking for."
        )

        # Clean unwanted formatting
        ai_response = ai_response.strip()

        return jsonify({
            "success": True,

            # User's original question
            "query": user_query,

            # Natural-language AI response
            "response": ai_response,

            # Navigation information
            "destination": result.get("destination", ""),
            "building": result.get("building", ""),
            "category": result.get("category", ""),
            "floor": result.get("floor", ""),
            "description": result.get("description", ""),

            # Route steps
            "route": result.get("route", []),

            # Matching confidence
            "confidence": result.get("confidence", 0)

        })

    except Exception as e:

        print("\n========== CHAT ERROR ==========")
        print(str(e))
        print("===============================\n")

        return jsonify({
            "success": False,
            "message": "I couldn't process that request. Please try asking about a campus location.",
            "response": "I'm having trouble processing your request right now. Please try again."
        }), 500


if __name__ == "__main__":

    print("=" * 60)
    print("CHRIST UNIVERSITY SMART CAMPUS NAVIGATOR")
    print("Flask API starting...")
    print("=" * 60)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )