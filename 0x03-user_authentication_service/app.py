#!/usr/bin/env python3
"""A function that creates a Flask app"""

from flask import Flask, jsonify, Response, request
from auth import Auth

Auth = Auth()
app = Flask(__name__)


@app.route("/")
def home() -> Response:
    """ Returns To Home"""
    message = {"message": "Bienvenue"}
    return jsonify(message)


@app.route('/users', methods=['POST'])
def users() -> Response:
    """This function registers Users"""
    if request.method == "POST":
        r_email = request.form.get("email")
        email = r_email.strip()
        r_password = request.form.get("password")
        password = r_password.strip()
        try:
            AUTH.register_user(email, password)
            message = jsonify({"email": email, "message": "user created"})
            return message
        except Exception:
            return jsonify({"message": "email already registered"})
    else:
        abort(400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
