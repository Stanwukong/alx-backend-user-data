#!/usr/bin/env python3
"""Authentication module for the API."""
from typing import List, TypeVar
from flask import request
import re


class Auth:
    """
    A class to manage API authentication.
    This class provides methods for handling API authentication
    by requiring authorizaion headers, identifying the current
    user, and excluding specified paths from authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for a given path.
        """
        if path is not None and excluded_paths is not None:
            for excluded_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if excluded_path[-1] == '*':
                    pattern = f'{excluded_path[0:-1]}.*'
                elif excluded_path[-1] == '/':
                    pattern = f'{excluded_path[0:-1]}/*'
                else:
                    pattern = f'{excluded_path}/*'
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from request.
        """
        if request is None:
            return None
        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Identifies the current user.
        """
        return None
