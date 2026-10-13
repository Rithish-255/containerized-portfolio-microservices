# Containerized Microservices Portfolio App (Node + Flask + NGINX)

This minor project demonstrates breaking a monolithic portfolio into containerized microservices and orchestrating them with Docker Compose or Kubernetes (Minikube).

Services:
- Flask API: /api/projects (JSON)
- Node.js Front-end: static UI that fetches /api/projects
- NGINX: reverse-proxy (routes /api -> Flask, / -> Node)

Quick run — Docker Compose
1. From project root:
   docker-compose build
   docker-compose up
2. Open http://localhost:8080

Quick run — Minikube (Kubernetes)
1. minikube start
2. eval $(minikube docker-env)
3. docker build -t flask-api:latest ./services/flask_api
   docker build -t node-frontend:latest ./services/node_frontend
   docker build -t custom-nginx:latest ./nginx
4. kubectl apply -f k8s/
5. minikube service nginx-service --url
6. Open returned URL in a browser.

Notes:
- If pushing images to DockerHub, update image names and imagePullPolicy in k8s manifests.
