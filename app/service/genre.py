from typing import List

from app.dao.genre import GenreDAO
from app.dao.model.genre import Genre
from app.service.base import BaseService


class GenreService(BaseService[Genre]):
    def __init__(self):
        super().__init__()
        self.dao = GenreDAO()

    def put_genre(self, gid: int, **kwargs):
        return self.dao.put_genre(gid, **kwargs)
