from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

# Database setup
DATABASE = '/data/users.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with users table"""
    with app.app_context():
        db = get_db()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        db.commit()
        
        # Add some sample users if table is empty
        cursor = db.execute('SELECT COUNT(*) as count FROM users')
        count = cursor.fetchone()['count']
        
        if count == 0:
            sample_users = [
                ('Alice Johnson', 'alice@example.com'),
                ('Bob Smith', 'bob@example.com'),
                ('Carol Davis', 'carol@example.com')
            ]
            for name, email in sample_users:
                try:
                    db.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
                except:
                    pass
            db.commit()
            print("✅ Sample users added to database")

# Initialize database on startup
init_db()

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "user-service",
        "database": "sqlite",
        "storage": "/data/users.db"
    })

@app.route('/users', methods=['GET'])
def get_users():
    db = get_db()
    users = db.execute('SELECT id, name, email FROM users ORDER BY id DESC').fetchall()
    return jsonify([dict(user) for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    
    db = get_db()
    try:
        cursor = db.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        db.commit()
        new_user = {
            'id': cursor.lastrowid,
            'name': name,
            'email': email
        }
        return jsonify(new_user), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "Email already exists"}), 409

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    db = get_db()
    cursor = db.execute('DELETE FROM users WHERE id = ?', (user_id,))
    db.commit()
    if cursor.rowcount == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200

@app.route('/stats', methods=['GET'])
def get_stats():
    db = get_db()
    total = db.execute('SELECT COUNT(*) as count FROM users').fetchone()['count']
    return jsonify({
        "total_users": total,
        "database": "SQLite",
        "storage_location": "/data/users.db"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
