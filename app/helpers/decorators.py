import jwt
from jwt.exceptions import PyJWTError
from flask import request
from functools import wraps
from typing import Callable

from app.constants import SECRET, ALGORITHMS


def user_required(user_role: list):
    def auth_required(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                return 'Could not verify', 401, {'WWW-Authenticate': 'Bearer error=Access denied'}

            data = request.headers['Authorization']
            token = data.split('Bearer ')[-1]

            try:
                data_token = jwt.decode(token, SECRET, algorithms=[ALGORITHMS])
            except PyJWTError:
                return 'Could not verify', 401, {'WWW-Authenticate': 'Bearer error=Access denied'}

            role = data_token.get('role', 'user')
            username = data_token.get('username')

            if role not in user_role:
                return 'Could not verify', 401, {'WWW-Authenticate': f'Bearer error=Access denied for {username}'}

            return func(*args, **kwargs)

        return wrapper

    return auth_required
