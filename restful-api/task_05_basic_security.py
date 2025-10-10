#!/bin/usr/python3

"""
Module qui permet de gérer la gestion des API
"""

from flask import Flask, request, jsonify
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
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):

    """
    Fonction qui permet de verifier le passworld
    """

    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username


@auth.error_handler
def unauthorized_error():

    """
    Fonction qui renvoie un message erreur
    """

    return jsonify({"error": "Unauthorized access"}), 401


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():

    """
    Fonction qui renvoir un message de réussite
    """

    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def get_login():

    """
    Fonction qui vérifie le login avec la méthode JWT
    """

    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"message": "Missing username or password"}), 400

    username = data["username"]
    password = data["password"]

    if (
    username not in users or
    not check_password_hash(users[username]["password"], password)
):
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]}
    )

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def get_JWT_authorisation():

    """
    Fonction qui verifie l'accès JWT
    """

    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():

    """
    Foction qui vérifie si c'est un admin
    """

    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin Access: Denied"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_missing_token(err):

    """
    Fonction qui renvoie un message d'erreur
    """

    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):

    """
    Fonction qui renvoie un message d'erreur
    """

    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):

    """
    Fonction qui renvoie un message d'erreur
    """

    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):

    """
    Fonction qui renvoie un message d'erreur
    """

    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(err):

    """
    Fonction qui renvoie un message d'erreur
    """

    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run(debug=True)
