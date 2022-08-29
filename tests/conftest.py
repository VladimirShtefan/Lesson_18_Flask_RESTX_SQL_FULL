import pytest

from app.app import create_app
from app.config import TestConfig
from app.setup_db import db
from load_fixtures import _load_fixtures


@pytest.fixture(scope='session')
def flask_app():
    test_app = create_app(TestConfig)

    client = test_app.test_client()

    with test_app.app_context():
        yield client


@pytest.fixture(scope='session')
def app_with_db(flask_app):
    db.create_all()
    _load_fixtures(db)
    yield db





