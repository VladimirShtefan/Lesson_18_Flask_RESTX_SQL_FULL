from sqlalchemy.exc import IntegrityError, InvalidRequestError

from app.dao.base import BaseDAO
from app.dao.model.genre import Genre
from app.exceptions import BadRequest
from logger import create_logger

logger = create_logger(__name__)


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre

    def put_genre(self, gid: int, **kwargs):
        genre_name = kwargs.get('name')
        try:
            self._db_session.query(Genre).filter_by(id=gid).update({'genre_name': genre_name})
        except IntegrityError as e:
            self._db_session.rollback()
            logger.info(e.orig)
            raise BadRequest(e.orig)
        except InvalidRequestError as e:
            self._db_session.rollback()
            logger.info(e.args[0])
            raise BadRequest(e.args[0])

    def add_genre(self, **kwargs) -> Genre:
        genre_name = kwargs.get('name')
        new_genre = Genre(genre_name=genre_name)
        self._db_session.add(new_genre)
        try:
            self._db_session.flush()
        except IntegrityError as e:
            self._db_session.rollback()
            logger.info(e.orig)
            raise BadRequest(e.orig)
        else:
            return new_genre
