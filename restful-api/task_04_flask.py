#!/usr/bin/python3

from flask import Flask
from flask import jsonify
import json


app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
}

@app.route("/")
def home ():
    return "<p>Welcome to the Flask API!</p>"

@app.route("/data")
def get_users():
    return jsonify(users), 200

@app.route("/status")
def status():
    return "<p>OK</p>"

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return ({"Error" :"User not found"}), 404

@app.route("/add_user/<username>")
def add_user(username):
    if username in users:
        return jsonify({"Error" : "User alredy exists"}), 400
    users[username] = {"name": username, "age": None, "city": None}

    return jsonify({"message": f"User '{username}' added successfully", "users": users}), 201

if __name__ == "__main__": app.run()