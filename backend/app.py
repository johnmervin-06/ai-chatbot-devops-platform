from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat')
def chat():
    return jsonify({
        "message": "Hello from AI Chatbot"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

