#!/usr/bin/env python3
"""A class that manages an API authentication"""

from flask import request
import os
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """A function that returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """A function that returns None"""
        return

    def current_user(self, request=None) -> TypeVar('User'):
        """A function that returns None"""
        return
