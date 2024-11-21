#!/usr/bin/env python3
"""A function that creates a Flask app"""

from flask import Flask, jsonify, Response, request, abort
from auth import Auth

app = Flask(__name__)
AUTH = AUTH()


@app.route("/")
def home() -> Response:
    """ Returns To Home"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'])
def users() -> str:
    """This function registers Users"""
    email, password = request.form.get("email"), request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
