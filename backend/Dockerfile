FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

ENV PORT=5000
EXPOSE 5000

# Talks to Ollama over the network (set OLLAMA_HOST env var, e.g. to
# http://ollama-service:11434 in k8s). Use Dockerfile.standalone instead
# if you want Ollama bundled into the same container for local demos.
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 2 --timeout 120 app:app
