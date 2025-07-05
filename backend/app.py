from flask import Flask, request, jsonify
from flask_cors import CORS
import cohere
import os
from dotenv import load_dotenv
from datetime import datetime
import re

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Load API key from .env
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found. Make sure it's set in the .env file.")

co = cohere.Client(COHERE_API_KEY)

# Log file path
LOG_FILE = "chat_log.txt"

@app.route("/")
def home():
    return "Welcome to IngreDecode API! Use POST /explain to chat about skincare."

@app.route("/explain", methods=["POST"])
def explain_ingredients():
    try:
        data = request.json
        conversation = data.get("conversation", [])

        if not conversation:
            return jsonify({"error": "No conversation provided"}), 400

        # Build chat-style prompt
        prompt = ""
        for turn in conversation:
            role = turn.get("role")
            content = turn.get("content", "")
            if role == "user":
                prompt += f"User: {content}\n"
            elif role == "bot":
                prompt += f"Bot: {content}\n"
        prompt += "Bot:"

        # Call Cohere API
        response = co.generate(
            model="command",
            prompt=prompt,
            max_tokens=700,
            temperature=0.5
        )

        # Extract and clean text
        raw_reply = (
            response.generations[0].text.strip()
            if response.generations and response.generations[0].text
            else "Sorry, I couldn't find an explanation."
        )

        # Remove markdown formatting like **bold**, _italics_
        cleaned = re.sub(r'(\*\*|\*|__|_)', '', raw_reply)

        # Ensure each list item starts on a new line
        formatted = re.sub(r'(?<!\n)(\s*)(\d+\.\s)', r'\n\2', cleaned)
        formatted = re.sub(r'(?<!\n)(\s*)(-\s)', r'\n\2', formatted)

        # Log conversation
        latest_user_msg = conversation[-1].get("content", "")
        log_entry = (
            f"\n---\nTimestamp: {datetime.now()}\n"
            f"User: {latest_user_msg}\n"
            f"Bot: {formatted}\n"
        )
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(log_entry)

        return jsonify({"reply": formatted})

    except Exception as e:
        print("Server error:", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
