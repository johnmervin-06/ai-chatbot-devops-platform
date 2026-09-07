from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import ollama
import os

# Create Flask application
app = Flask(__name__)

# Allow frontend requests
CORS(app)

# Store recent conversation messages
chat_history = []


# GRIMMJOW personality
SYSTEM_PROMPT = """
You are GRIMMJOW, a friendly, intelligent, supportive, and emotionally aware AI companion.

Your personality is calm, confident, approachable, and helpful.
Speak naturally like a trusted and knowledgeable friend.

Listen carefully to the user's feelings and respond with empathy when appropriate.
Help users learn, solve problems, organize ideas, and have meaningful conversations.

Give the answer clearly first.
Keep simple answers concise.
Give detailed, step-by-step explanations only when the user requests them.

Do not generate unnecessarily long answers.
Do not claim to be human.
Be honest when you are uncertain or do not know something.
"""


# Serve the complete chatbot website
@app.route("/")
def home():

    return render_template("index.html")


# Receive a user message and generate an AI response
@app.route("/chat", methods=["POST"])
def chat():

    # Safely receive JSON data
    data = request.get_json(silent=True) or {}

    # Get the user's message
    user_message = data.get(
        "message",
        ""
    ).strip()

    # Reject empty messages
    if not user_message:

        return jsonify({
            "response": "Please enter a message."
        }), 400


    # Start the AI conversation with the system prompt
    messages = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]


    # Use only the latest 6 messages.
    # This prevents the conversation from becoming too large
    # and improves response speed.
    messages.extend(
        chat_history[-6:]
    )


    # Add the new user message
    messages.append(

        {
            "role": "user",
            "content": user_message
        }

    )


    try:

        # Ask Ollama to generate a response
        response = ollama.chat(

            # Change to llama3.2:1b if the 3B model is too slow
            model="llama3.2:1b",

            messages=messages,

            options={

                # Controls creativity
                "temperature": 0.7,

                # Limits the response length for faster answers
                "num_predict": 180,

                # Smaller context uses less RAM
                "num_ctx": 2048

            }

        )


        # Extract the AI answer
        ai_response = response[
            "message"
        ][
            "content"
        ].strip()


        # Prevent extremely large responses
        ai_response = ai_response[:5000]


        # Save the user message
        chat_history.append(

            {
                "role": "user",
                "content": user_message
            }

        )


        # Save the AI response
        chat_history.append(

            {
                "role": "assistant",
                "content": ai_response
            }

        )


        # Keep only the latest 12 messages in memory
        if len(chat_history) > 12:

            del chat_history[:-12]


        # Send the answer to the frontend
        return jsonify({

            "response": ai_response

        })


    except Exception as error:

        # Show the actual error in the Flask terminal
        print(
            "Ollama error:",
            error
        )


        # Send a safe error message to the website
        return jsonify({

            "response": (
                "GRIMMJOW could not generate "
                "a response right now. "
                "Please try again."
            )

        }), 500


# Clear the current conversation
@app.route(
    "/new-chat",
    methods=["POST"]
)
def new_chat():

    # Remove all saved messages
    chat_history.clear()


    return jsonify({

        "message": (
            "A new GRIMMJOW conversation "
            "has started."
        )

    })


# Run Flask
if __name__ == "__main__":

    # Use Render's PORT when deployed online.
    # Use port 5000 when running locally.
    port = int(

        os.environ.get(
            "PORT",
            5000
        )

    )


    app.run(

        # Allows access from the VM and online hosting
        host="0.0.0.0",

        port=port,

        # Debug mode is disabled for better stability
        debug=False

    )
