from flask_restx import fields

from app.setup_api import api
from app.setup_db import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False, default='user')


user_model = api.model(
    'User',
    {
        'id': fields.Integer(required=True, example=12),
        'username': fields.String(max_length=50, required=True, example='username'),
        'password': fields.String(max_length=255, required=True, example='password'),
        'role': fields.String(max_length=30, required=True, example='user'),
    }
)