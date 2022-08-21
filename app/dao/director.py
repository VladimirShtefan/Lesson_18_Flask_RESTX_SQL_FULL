from sqlalchemy.exc import IntegrityError, InvalidRequestError

from app.dao.base import BaseDAO
from app.dao.model.director import Director
from app.exceptions import BadRequest
from logger import create_logger

logger = create_logger(__name__)


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director

    def put_director(self, did: int, **kwargs):
        director_name = kwargs.get('name')
        try:
            self._db_session.query(Director).filter_by(id=did).update({'director_name': director_name})
        except IntegrityError as e:
            self._db_session.rollback()
            logger.info(e.orig)
            raise BadRequest(e.orig)
        except InvalidRequestError as e:
            self._db_session.rollback()
            logger.info(e.args[0])
            raise BadRequest(e.args[0])
