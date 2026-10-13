from flask import Flask, jsonify
app = Flask(__name__)

PROJECTS = [
    {"id": 1, "title": "Portfolio Website", "description": "Personal portfolio site"},
    {"id": 2, "title": "API Service", "description": "Microservice providing project data"},
    {"id": 3, "title": "CI/CD Demo", "description": "Automated pipeline example"}
]

@app.route("/api/projects")
def projects():
    return jsonify(PROJECTS)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
