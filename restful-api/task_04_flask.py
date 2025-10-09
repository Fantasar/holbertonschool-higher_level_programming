#!/usr/bin/python3

"""
Module qui permet de simuler un serveur et de gérer plusieurs commandes
comme l'ajout d'un utilisateur dans un dictionnaire
"""

from flask import Flask
from flask import jsonify
import json


app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}


@app.route("/")
def home():
    """
    Méthode instance pour initialiser la page de garde
    """

    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def get_users():
    """
    Méthode d'instance pour afficher les utilisateurs de la
    base de donnée
    """

    return jsonify(users), 200


@app.route("/status")
def status():
    """
    Méthode d'instance pour indiquer l'état de la page web
    """
    return "<p>OK</p>"


@app.route("/users/<username>")
def get_user(username):
    """
    Méthode pour recherche un utilisateur particulier
    dans la base de donnée
    """

    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return ({"Error": "User not found"}), 404


@app.route("/add_user/<username>")
def add_user(username):
    """
    Méthode pour ajouter un utilisateur dans la base de donnée
    """

    if username in users:
        return jsonify({"Error": "User alredy exists"}), 400
    users[username] = {"name": username, "age": None, "city": None}

    return jsonify({"message": f"User '{username}' added successfully",
                    "users": users}), 201


if __name__ == "__main__":
    app.run()
