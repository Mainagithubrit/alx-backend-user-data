#!/usr/bin/env python3
"""A class that manages an API authentication"""

from flask import request
import os
from typing import List, TypeVar


class Auth:
    """A class to manage an API"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A function that returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """A function that returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A function that returns None"""
        return None
