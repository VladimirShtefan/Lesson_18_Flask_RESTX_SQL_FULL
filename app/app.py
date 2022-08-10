from flask import Flask
from flask_restx import Api

from app.setup_db import db
from app.views.view_movies import movie_ns
from logger import create_logger

logger = create_logger(__name__)


def create_app(config_object) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    logger.info('app created')
    return application


def register_extensions(app: Flask):
    db.init_app(app)
    api = Api()
    api.init_app(app)
    api.add_namespace(movie_ns)
    logger.info('register extensions complete')