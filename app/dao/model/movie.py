from flask_restx import fields

from app.dao.model.director import Director, director_model
from app.dao.model.genre import Genre, genre_model
from app.setup_api import api
from app.setup_db import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255), unique=True)
    year = db.Column(db.Integer, db.CheckConstraint('year >= 0'))
    rating = db.Column(db.Float, db.CheckConstraint('rating >= 0.0 and rating <= 10.0'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre', cascade='all, delete')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director', cascade='all, delete')


movie_model = api.model(
    'Movie',
    {
        'id': fields.Integer(required=True),
        'title': fields.String(max_length=50, required=True),
        'description': fields.String(max_length=255),
        'trailer': fields.String(max_length=255),
        'year': fields.Integer(min=0),
        'rating': fields.Float(min=0.0, max=10.0),
        'genre_id': fields.Integer(required=True),
        'director_id': fields.Integer(required=True),
        'genre': fields.Nested(genre_model),
        'director': fields.Nested(director_model),
    }
)
