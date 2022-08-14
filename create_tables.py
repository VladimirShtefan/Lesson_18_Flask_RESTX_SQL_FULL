from app.app import create_app
from app.config import Config
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from app.setup_db import db


def _create_tables():
    db.create_all()


if __name__ == '__main__':
    app = create_app(Config)
    with app.app_context():
        _create_tables()
