from flask import Flask, request, escape
import subprocess
import sqlite3
import hashlib

app = Flask(__name__)

# Vulnerability 1: SQL Injection (CWE-89)
@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '" + user_id + "'")
    return str(cursor.fetchone())

# Vulnerability 2: Command Injection (CWE-78)
@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.check_output("ping -c 1 " + host, shell=True)
    return result

# Vulnerability 3: Reflected XSS (CWE-79)
@app.route("/search")
def search():
    query = request.args.get("q")
    safe_query = escape(query if query is not None else "")
    return "<h1>Results for: " + safe_query + "</h1>"

# Vulnerability 4: Weak hashing (CWE-328)
@app.route("/register")
def register():
    password = request.args.get("password")
    hashed = hashlib.md5(password.encode()).hexdigest()
    return "Stored hash: " + hashed

# Vulnerability 5: Hardcoded secret (CWE-798)
API_KEY = "sk-1234567890abcdef"

if __name__ == "__main__":
    app.run(debug=True)
