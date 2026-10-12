import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    user_message = data.get('message', '').strip()

    if not user_message:
        return jsonify({'error': 'Message cannot be empty'}), 400

    try:
        response = ollama.chat(
            model='llama3.2',
            messages=[
                {"role": "system", "content": "You are M3 AI, a helpful and concise assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        reply_content = response['message']['content']
        return jsonify({'reply': reply_content, 'response': reply_content})
    except Exception as e:
        return jsonify({
            'error': str(e),
            'reply': '⚠️ Could not connect to local Ollama. Ensure Ollama is running (`ollama serve`).'
        }), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
EOF
