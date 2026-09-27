#!/bin/sh
set -e

# Start the Ollama daemon in the background
ollama serve &
OLLAMA_PID=$!

# Wait for it to accept connections before pulling/serving
until ollama list >/dev/null 2>&1; do
  echo "Waiting for Ollama daemon to start..."
  sleep 1
done

# Pull the model if it isn't already present in the image/volume
if ! ollama list | grep -q "${OLLAMA_MODEL:-llama3.2:1b}"; then
  echo "Pulling model ${OLLAMA_MODEL:-llama3.2:1b}..."
  ollama pull "${OLLAMA_MODEL:-llama3.2:1b}"
fi

# Start the Flask app under gunicorn
exec gunicorn --bind 0.0.0.0:"${PORT:-5000}" --workers 2 --timeout 120 app:app

# (only reached if gunicorn exits)
kill "$OLLAMA_PID"
