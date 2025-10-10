#!/bin/usr/python3

from flask import Flask , request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required, get_jwt


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["SECRET_KEY"] = "test"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
    "admin2": {"username": "admin2", "password": generate_password_hash("plouf"), "role": "admin"},
    "admin3": {"username": "admin3", "password": generate_password_hash("plouf"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username

@app.route("/basic-protected", methods=["GET"])
def get_authorisation():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def get_login():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def get_JWT_authorisation():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"message": "Admin Access: Denied"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run()
