from flask import Flask, g

from app.exceptions import BadRequest
from app.setup_api import api
from app.setup_db import db
from app.views.view_directors import director_ns
from app.views.view_genres import genre_ns
from app.views.view_movies import movie_ns
from logger import create_logger

logger = create_logger(__name__)


def create_app(config_object) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_object)
    register_extensions(application)
    logger.info('app created')

    @application.before_request
    def open_session():
        g.session = db.session

    @application.after_request
    def close_session(response):
        if getattr(g, 'session'):
            try:
                g.session.commit()
            except:
                g.session.rollback()
            finally:
                g.session.close()
        return response
    return application


def register_extensions(app: Flask):
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)

    @api.errorhandler(BadRequest)
    def bad_request_400(e: BadRequest):
        return {
                   'error': str(e.message),
                   'code': e.code
               }, e.code
