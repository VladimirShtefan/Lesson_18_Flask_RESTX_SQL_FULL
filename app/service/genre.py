from typing import List

from app.dao.genre import GenreDAO
from app.dao.model.genre import Genre
from app.service.base import BaseService


class GenreService(BaseService[Genre]):
    def __init__(self):
        super().__init__()
        self.dao = GenreDAO()

    def get_all_genres(self) -> List[Genre]:
        return self.dao.get_all_items()

    def get_genre(self, gid: int) -> Genre:
        return self.dao.get_one_by_id(gid)
