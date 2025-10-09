#!/usr/bin/python3

"""
Module qui permet de simuler un serveur et de gérer plusieurs commandes
comme l'ajout d'un utilisateur dans un dictionnaire
"""

from flask import Flask
from flask import jsonify, request


app = Flask(__name__)

users = {}

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


@app.route("/", methods=["GET"])
def home():
    """
    Méthode instance pour initialiser la page de garde
    """

    return "<p>Welcome to the Flask API!</p>"


@app.route("/data", methods=["GET"])
def get_users():
    """
    Méthode d'instance pour afficher les utilisateurs de la
    base de donnée
    """

    return jsonify(list(users.keys())), 200


@app.route("/status", methods=["GET"])
def status():
    """
    Méthode d'instance pour indiquer l'état de la page web
    """
    return "<p>OK</p>"


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Méthode pour recherche un utilisateur particulier
    dans la base de donnée
    """

    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return ({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user(username):
    """
    Méthode pour ajouter un utilisateur dans la base de donnée
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Users already exists"}), 400

    users[username] = {
        "username": username,
        "name": name,
        "age": age,
        "city": city
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
