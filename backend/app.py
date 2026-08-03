from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import ollama
import os

app = Flask(__name__)

CORS(app)

chat_history = []

SYSTEM_PROMPT = """
You are GRIMMJOW AI, a friendly, supportive, and helpful AI companion.

Be warm, natural, and easy to talk to.
Give clear answers first and add details only when useful.
For simple questions, keep your answers concise.
"""


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get(
        "message",
        ""
    ).strip()

    if not user_message:
        return jsonify({
            "response": "Please enter a message."
        }), 400

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(
        chat_history[-6:]
    )

    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    try:

        response = ollama.chat(
            model="llama3.2:3b",
            messages=messages,
            options={
                "temperature": 0.7,
                "num_predict": 250,
                "num_ctx": 2048
            }
        )

        ai_response = (
            response["message"]["content"]
        )

        chat_history.append(
            {
                "role": "user",
                "content": user_message
            }
        )

        chat_history.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

        return jsonify(
            {
                "response": ai_response
            }
        )

    except Exception as error:

        print(
            "Ollama error:",
            error
        )

        return jsonify(
            {
                "response": (
                    "I am having trouble connecting "
                    "to my AI model. Please try again."
                )
            }
        ), 500


@app.route(
    "/new-chat",
    methods=["POST"]
)
def new_chat():

    chat_history.clear()

    return jsonify(
        {
            "message": "New chat started."
        }
    )


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )
