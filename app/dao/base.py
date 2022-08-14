from typing import TypeVar, Generic, List
from flask import g

from app.setup_db import db

T = TypeVar('T', bound=db.Model)


class BaseDAO(Generic[T]):
    __model__ = db.Model

    def __init__(self):
        self._db_session = g.session

    def get_one_by_id(self, id: int) -> T:
        return self._db_session.query(self.__model__).get_or_404(id)

    def delete_row(self, id: int):
        movie = self._db_session.query(self.__model__).get_or_404(id)
        self._db_session.delete(movie)

    def update_row(self, id: int, **kwargs) -> None:
        self._db_session.query(self.__model__).filter_by(id=id).update(kwargs)
        # self._db_session.commit()