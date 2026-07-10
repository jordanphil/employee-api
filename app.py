from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "John Doe", "department": "IT"},
    {"id": 2, "name": "Jane Smith", "department": "HR"}
]

@app.route("/")
def home():
    return jsonify({"status": "ok", "version": "1.0.2"})

@app.route("/api/employees")
def get_employees():
    return jsonify(employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
