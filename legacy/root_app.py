from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "message":
        "AI Chatbot backend is running"

    })


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()


    user_message = data.get(
        "message",
        ""
    )


    # Replace this section with
    # your actual AI chatbot logic

    ai_response = (

        "You said: "

        + user_message

    )


    return jsonify({

        "response":
        ai_response

    })


if __name__ == "__main__":

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
