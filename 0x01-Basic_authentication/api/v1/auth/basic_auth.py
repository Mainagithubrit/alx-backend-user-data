#!/usr/bin/env python3
"""A class that inherits from Auth"""
from models.user import User
from typing import TypeVar
from .auth import Auth
import base64


class BasicAuth(Auth):
    """ A class that returns Base64 authorization header
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns a base64 header"""
        if authorization_header is None:
            return
        if not isinstance(authorization_header, str):
            return
        if not authorization_header.startswith('Basic '):
            return
        value = authorization_header.split(' ')[1]
        return value

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str,
    ) -> str:
        """This returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except (ValueError, TypeError):
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str,
    ) -> (str, str):
        """This fuctions takes a Base64-decoded string
        seperated by a colon and returns a tuple """
        if decoded_base64_authorization_header is None or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, password = decoded_base64_authorization_header.split(":", 1)

        return email, password

    def user_object_from_credentials(
        self, user_email: str,
        user_pwd: str,
    ) -> TypeVar('User'):
        """A function that return a user instance based
        on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search(user_email)
        except KeyError:
            return None
        except Exception:
            return None
        if user is None:
            return None
        for user in users:
            if not user.is_valid_password(user_pwd):
                return user
        return None
