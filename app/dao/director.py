from sqlalchemy.exc import IntegrityError, InvalidRequestError

from app.dao.base import BaseDAO
from app.dao.model.director import Director
from app.exceptions import BadRequest


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director

    def put_director(self, did: int, **kwargs) -> None:
        director_name = kwargs.get('name')
        try:
            self._db_session.query(self.__model__).filter_by(id=did).update({'director_name': director_name})
        except IntegrityError as e:
            self._db_session.rollback()
            self.logger.info(e.orig)
            raise BadRequest(e.orig)
        except InvalidRequestError as e:
            self._db_session.rollback()
            self.logger.info(e.args[0])
            raise BadRequest(e.args[0])

    def add_director(self, **kwargs) -> Director:
        director_name = kwargs.get('name')
        new_director = self.__model__(director_name=director_name)
        self._db_session.add(new_director)
        try:
            self._db_session.flush()
        except IntegrityError as e:
            self._db_session.rollback()
            self.logger.info(e.orig)
            raise BadRequest(e.orig)
        else:
            return new_director
