from flask_restx import fields

from app.setup_api import api
from app.setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


director_model = api.model(
    'Director',
    {
        'pk': fields.Integer(attribute='id', required=True),
        'name': fields.String(required=True, max_length=50),
    }
)