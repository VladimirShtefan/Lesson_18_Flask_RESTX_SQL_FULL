from app.dao.base import BaseDAO
from app.dao.model.genre import Genre


class GenreDAO(BaseDAO[Genre]):
    __model__ = Genre
