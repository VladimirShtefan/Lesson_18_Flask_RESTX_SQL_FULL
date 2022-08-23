from flask import request, abort
from functools import wraps
from typing import Callable


def auth_required(func: Callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        if data := request.headers.get('Authorization'):
            token = data.split('Bearer ')[-1]
        else:
            abort(401)

        data = request.headers['Authorization']
