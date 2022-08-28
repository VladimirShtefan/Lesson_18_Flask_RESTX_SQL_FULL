import pytest

from app.app import create_app
from app.config import TestConfig
from app.setup_db import db as database


@pytest.fixture(scope='session')
def app():
    _app = create_app(TestConfig)
    with _app.app_context():
        database.init_app(_app)
        yield _app


@pytest.fixture
def db(app):
    database.drop_all()
    database.create_all()
    database.session.commit()
    return database


@pytest.fixture
def client(db, app):
    with app.test_client() as client:
        yield client
