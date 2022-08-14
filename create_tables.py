from app.app import create_app
from app.config import Config
from app.setup_db import db


def _create_tables():
    db.create_all()


if __name__ == '__main__':
    app = create_app(Config)
    with app.app_context():
        _create_tables()
