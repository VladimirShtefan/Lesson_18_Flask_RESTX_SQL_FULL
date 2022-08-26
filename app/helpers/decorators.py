import jwt
from jwt.exceptions import PyJWTError
from flask import request
from flask_restx import abort
from functools import wraps
from typing import Callable

from app.constants import SECRET, ALGORITHMS


def user_required(user_role: tuple):
    def auth_required(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if 'Authorization' not in request.headers:
                abort(401, 'Could not verify', error={'WWW-Authenticate': 'Bearer error=Access denied'})

            data = request.headers['Authorization']
            token = data.split('Bearer ')[-1]

            try:
                data_token = jwt.decode(token, SECRET, algorithms=[ALGORITHMS])
            except PyJWTError:
                abort(401, 'Could not verify', error={'WWW-Authenticate': 'Bearer error=Access denied'})
            else:
                role = data_token.get('role', 'user')
                username = data_token['username']

                if role not in user_role:
                    abort(401, 'Could not verify', error={
                        'WWW-Authenticate': f'Bearer error=Access denied for {username}'
                    })

                return func(*args, **kwargs, username=data_token['username'])

        return wrapper

    return auth_required
