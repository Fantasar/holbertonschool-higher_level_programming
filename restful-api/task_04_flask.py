#!/usr/bin/python3

"""
Module qui permet de simuler un serveur et de gérer plusieurs commandes
comme l'ajout d'un utilisateur dans un dictionnaire
"""

from flask import Flask
from flask import jsonify, request


app = Flask(__name__)

users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Méthode instance pour initialiser la page de garde
    """

    return "Welcome to the Flask API!"


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
    return "OK"


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
def add_user():
    """
    Méthode pour ajouter un utilisateur dans la base de donnée
    """

    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
