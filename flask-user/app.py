from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory database
users = [
    {"id": "1", "name": "Alice Johnson", "email": "alice@example.com"},
    {"id": "2", "name": "Bob Smith", "email": "bob@example.com"},
]

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "user-service"})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": str(len(users) + 1),
        "name": data.get('name'),
        "email": data.get('email')
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/')
def root():
    return jsonify({"message": "User Service is running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
