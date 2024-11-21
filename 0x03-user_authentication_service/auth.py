#!/usr/bin/env python3
"""a hash password method"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """a function that hashes a password using bcrypt"""
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()

    hashed_pwd = bcrypt.hashpw(password_bytes, salt)

    return hashed_pwd
