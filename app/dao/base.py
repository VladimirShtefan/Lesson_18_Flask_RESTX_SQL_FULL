from typing import TypeVar, Generic, List, Optional
from flask import g

from app.setup_db import db
from sqlalchemy.orm.scoping import scoped_session

T = TypeVar('T', bound=db.Model)


class BaseDAO(Generic[T]):
    __model__ = db.Model

    def __init__(self, db_session: Optional[scoped_session] = None):
        self._db_session = getattr(g, 'session', db_session)

    def get_one_by_id(self, id: int) -> T:
        return self._db_session.query(self.__model__).get_or_404(id, description='Id not found')

    def delete_row(self, id: int) -> None:
        movie = self._db_session.query(self.__model__).get_or_404(id, description='Id not found')
        self._db_session.delete(movie)

    def get_all_items(self) -> List[T]:
        return self._db_session.query(self.__model__).all()
