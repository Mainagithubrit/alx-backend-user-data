#!/usr/bin/env python3
"""A class that inherits from Auth"""

from api.v1.auth.auth import Auth


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
