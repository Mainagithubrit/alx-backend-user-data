#!/usr/bin/env python3
"""A class that manages an API authentication"""

from flask import request
import os
from typing import List, TypeVar


class Auth:
    """A class to manage an API"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A function that returns true if not a path, if excluded_paths
        is None and returns false if path is excluded_paths"""
        if path and not path.endswith('/'):
            path = path + '/'
        if is path is None:
            return True
        if path not in excluded_paths:
            return True
        if not excluded_paths or excluded_paths == []:
            return True
        if path in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """A function that checks for authorization"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A function that returns None"""
        return None
