# AI Chatbot DevOps Platform

A Flask + Ollama chatbot ("GRIMMJOW"), containerized and deployed with a
Docker → Jenkins → Terraform (AWS EC2) → Kubernetes pipeline.

## Stack (matches what's actually in this repo)
- **Backend:** Flask + `ollama` (local `llama3.2:1b` model) — `backend/app.py`
- **Frontend:** static HTML/JS chat UI — `backend/templates/index.html`
- **Containerization:** Docker (`backend/Dockerfile` for k8s use,
  `backend/Dockerfile.standalone` for a single-container local demo)
- **CI/CD:** Jenkins (`Jenkinsfile`) — build, test, Trivy scan, push, deploy
- **Infra as Code:** Terraform (`terraform/`) — provisions an EC2 instance
- **Orchestration:** Kubernetes (`k8s/deployment.yaml`) — chatbot + Ollama
  as separate Deployments/Services

> Not used (removed from the docs to avoid confusion): AWS Lex, GitHub Actions.
> `legacy/` holds earlier draft versions of the app that are no longer deployed.

## Local development
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
ollama pull llama3.2:1b     # requires Ollama installed locally: https://ollama.com
python app.py               # http://127.0.0.1:5000
```

## Docker (standalone, bundles Ollama)
```bash
cd backend
docker build -t chatbot-backend:standalone -f Dockerfile.standalone .
docker run -p 5000:5000 chatbot-backend:standalone
```

## Kubernetes (Ollama as a separate service)
```bash
cd backend
docker build -t chatbot-backend:v1 .
kubectl apply -f ../k8s/deployment.yaml
```

## Terraform (provisions the EC2 host)
```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars   # fill in your key_name and IP
terraform init
terraform plan
terraform apply
```

## Author
P. John Mervin
