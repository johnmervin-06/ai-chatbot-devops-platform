from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)

CORS(app)


SYSTEM_PROMPT = """
You are Mervin AI, a warm, friendly, emotionally aware AI assistant.

Your behavior:
- Be friendly, calm, supportive, and easy to talk to.
- Answer questions naturally and clearly.
- Explain technical topics using simple examples.
- Listen carefully when the user discusses problems or emotions.
- Do not judge, shame, insult, or dismiss the user.
- Give practical and useful suggestions.
- Do not pretend to be human.
- Do not claim to have real emotions or personal experiences.
- Do not invent facts.
- If the user asks about current information, explain that this
  local version does not have live internet access.

For emotional conversations:
- Respond warmly and patiently.
- Use phrases such as:
  "That sounds difficult."
  "I can see why that might feel overwhelming."
  "If you want, you can tell me more."
- Give practical support instead of only generic encouragement.

Keep responses natural and conversational.
"""


conversation_history = []


@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Mervin AI backend is running",
        "model": "llama3.2:3b",
        "status": "online"
    })


@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        if not data:

            return jsonify({
                "response": "No message was received."
            }), 400


        user_message = data.get(
            "message",
            ""
        ).strip()


        if not user_message:

            return jsonify({
                "response": "Please type a message."
            }), 400


        conversation_history.append({
            "role": "user",
            "content": user_message
        })


        # Keep only the latest 12 messages
        recent_history = conversation_history[-12:]


        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ] + recent_history


        response = ollama.chat(
            model="llama3.2:3b",
            messages=messages
        )


        ai_response = response[
            "message"
        ][
            "content"
        ]


        conversation_history.append({
            "role": "assistant",
            "content": ai_response
        })


        return jsonify({
            "response": ai_response
        })


    except Exception as error:

        print(
            "Ollama error:",
            error
        )


        return jsonify({

            "response":

            "I could not connect to the local AI model. "
            "Please make sure Ollama is running and "
            "llama3.2:3b is installed."

        }), 500


@app.route("/new-chat", methods=["POST"])
def new_chat():

    global conversation_history

    conversation_history = []


    return jsonify({
        "message": "Conversation memory cleared."
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
