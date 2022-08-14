from flask_restx import fields

from app.setup_api import api
from app.setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


genre_model = api.model(
    'Genre',
    {
        'pk': fields.Integer(attribute='id', required=True),
        'name': fields.String(required=True, max_length=50),
    }
)
