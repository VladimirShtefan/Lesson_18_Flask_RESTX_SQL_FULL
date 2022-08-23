import base64
import calendar
import hashlib
import re
import hmac

import jwt
from datetime import datetime, timedelta
from functools import update_wrapper
from typing import Callable

from app.constants import SECRET, ALGORITHMS
from app.dao.model.user import User
from app.dao.user import UserDAO
from app.exceptions import ValidationError, UserNotFound, InvalidPassword
from app.helpers.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.service.base import BaseService

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'


class UserService(BaseService[User]):
    def __init__(self):
        super().__init__()
        self.dao = UserDAO()

    @staticmethod
    def get_hash(password: str):
        hash_password = hashlib.pbkdf2_hmac(
            'sha512',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )
        return hash_password

    @staticmethod
    def check_reliability(password: str):
        if re.match(pattern, password) is None:
            raise ValidationError('Password has incorrect format.')
        return password

    @staticmethod
    def generate_tokens(data: dict):
        delay_30_min = datetime.utcnow() + timedelta(minutes=20)
        delay_90_days = datetime.utcnow() + timedelta(days=90)
        data['exp'] = calendar.timegm(delay_30_min.timetuple())
        access_token = jwt.encode(data, SECRET, algorithm=ALGORITHMS)
        data['exp'] = calendar.timegm(delay_90_days.timetuple())
        refresh_token = jwt.encode(data, SECRET, algorithm=ALGORITHMS)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }

    def search_user(self, **kwargs):
        username: str = kwargs.get('username')
        password: bytes = self.get_hash(kwargs.get('password'))
        user = self.dao.search_user(username)

        if user is None:
            raise UserNotFound(f'User with username:{username}, not found')

        if not hmac.compare_digest(user.password, password):
            raise InvalidPassword('Invalid password')

        data = {'username': user.username, 'role': user.role.name}
        return self.generate_tokens(data)

    def create_user(self, **kwargs):
        password: bytes = self.get_hash(self.check_reliability(kwargs.get('password')))
        username: str = kwargs.get('username')
        role: str = kwargs.get('role')
        return self.dao.create_user(username, password, role)
