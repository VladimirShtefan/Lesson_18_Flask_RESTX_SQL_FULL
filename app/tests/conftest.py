from flask import Flask
from unittest.mock import patch
import pytest
import logging

from app.config import TestConfig
from app.dao.movie import MovieDAO
from app.setup_db import db
from load_fixtures import _load_fixtures


@pytest.fixture(autouse=True)
def create_app():
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    with app.app_context():
        yield app.test_client()


@pytest.fixture(autouse=True)
def db_session(create_app):
    db.init_app(create_app.application)
    with create_app.application.app_context():
        db.create_all()
        _load_fixtures()
    yield db


@pytest.fixture()
def movie_dao(db_session):
    with patch.object(MovieDAO, '__init__', lambda self: None):
        patch_movie_dao = MovieDAO()
        patch_movie_dao._db_session = db_session.session
        patch_movie_dao.logger = logging.getLogger('test')
        yield patch_movie_dao
