#!/usr/bin/env python3
"""a hash password method"""
import bcrypt
from sqlalchemy.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """a function that hashes a password using bcrypt"""
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hashed_pwd = bcrypt.hashpw(password_bytes, salt)

    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """This function takes an email and password and returns a User"""
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass

        hashed_pwd = _hash_password(password)

        new_user = self._db.add_user(
            email=email,
            hashed_password=hashed_pwd.decode("utf-8"))
        self._db

        return new_user
