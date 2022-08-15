from app.dao.base import BaseDAO
from app.dao.model.director import Director


class DirectorDAO(BaseDAO[Director]):
    __model__ = Director
