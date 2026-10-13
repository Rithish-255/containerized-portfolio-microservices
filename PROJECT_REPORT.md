# Containerized Microservices Portfolio App
# College Project Report

## 1. Title
Containerized Microservices Portfolio App

## 2. Abstract
This project demonstrates the design and implementation of a microservices-based web application using Docker, NGINX, Node.js, Flask, and Kubernetes (Minikube). The application is a portfolio website where the front-end UI is served by a Node.js service, the project data is provided by a Flask API, and NGINX acts as a reverse proxy. Each service is containerized using Docker and orchestrated using Kubernetes pods and services. This project provides a practical understanding of decomposing a monolithic web application into smaller, independently deployable microservices.

## 3. Objectives
- To design a portfolio app using microservices architecture
- To separate front-end and backend functionality
- To implement API using Flask
- To implement UI using Node.js
- To route requests using NGINX
- To run services with Docker
- To orchestrate using Kubernetes (Minikube)
- To understand microservice communication and system deployment

## 4. Problem Statement
Traditional monolithic applications create dependency between user interface, business logic, and data access. As the application grows, updates become difficult and deployment becomes risky. The need is to divide the application into independent components so that they can be developed, tested, deployed, and scaled independently.

## 5. Technologies Used
- Docker
- Docker Compose
- Kubernetes (Minikube)
- NGINX
- Node.js
- Flask
- Python
- HTML/CSS
- YAML

## 6. System Architecture
The system consists of three main services:

- Front-end service: Node.js application serving portfolio UI
- Backend service: Flask API returning project data
- Reverse proxy: NGINX routing browser requests to the correct service

Client -> NGINX -> Node.js Front-end / Flask API

## 7. Modules
### 7.1 Front-end Module
- Serves the portfolio page using Express
- Displays project cards dynamically
- Fetches data from /api/projects

### 7.2 Backend Module
- Flask application exposes /api/projects
- Returns JSON data for projects

### 7.3 Proxy Module
- NGINX routes:
  - / -> Node.js
  - /api/* -> Flask

### 7.4 Containerization and Orchestration
- Dockerfiles for each service
- docker-compose.yml for local execution
- k8s YAML files for Kubernetes deployment

## 8. Implementation
The project uses:

1. Flask API to provide portfolio data.
2. Node.js front-end to display the page.
3. NGINX as the reverse proxy.
4. Docker for containerization.
5. Kubernetes for orchestration in Minikube.

## 9. Execution
### Run Locally Using Docker Compose
```bash
docker-compose build
docker-compose up
```
Open:
```text
http://localhost:8080
```

### Check API Output
```bash
curl http://localhost:8080/api/projects
```
Expected output:
```json
[
  {"id":1,"title":"Portfolio Website","description":"Personal portfolio site"},
  {"id":2,"title":"API Service","description":"Microservice providing project data"},
  {"id":3,"title":"CI/CD Demo","description":"Automated pipeline example"}
]
```

### Kubernetes (Minikube)
```bash
minikube start
eval $(minikube docker-env)
docker build -t flask-api:latest ./services/flask_api
docker build -t node-frontend:latest ./services/node_frontend
docker build -t custom-nginx:latest ./nginx
kubectl apply -f k8s/
minikube service nginx-service --url
```

## 10. Expected Output
The browser will display:

- Portfolio (Microservices)
- Portfolio Website
- API Service
- CI/CD Demo

The Flask API returns JSON data in the following format:

```json
[
  {"id":1,"title":"Portfolio Website","description":"Personal portfolio site"},
  {"id":2,"title":"API Service","description":"Microservice providing project data"},
  {"id":3,"title":"CI/CD Demo","description":"Automated pipeline example"}
]
```

## 11. Observations
- Microservices help modularize application components.
- NGINX provides efficient routing.
- Docker simplifies environment consistency.
- Kubernetes makes scaling and service management easier.
- This approach is industry-standard for cloud-native application development.

## 12. Advantages
- Independent component deployment
- Better fault isolation
- Easier maintenance and updates
- Improved scalability
- Modern architecture pattern

## 13. Limitations
- More complex than monoliths
- Requires container and Kubernetes knowledge
- Additional deployment configuration required

## 14. Conclusion
The Containerized Microservices Portfolio App demonstrates the concept of splitting a monolithic application into smaller autonomous services. It shows how Node.js, Flask, NGINX, Docker, and Kubernetes work together to build and deploy a scalable portfolio site. The project highlights the practical value of microservices architecture in modern software development.

## 15. Declaration
I declare that this project is my original work and has been completed with due care and understanding of the subject.

Signature:
[Student Name]

