from typing import List

from app.dao.director import DirectorDAO
from app.dao.model.director import Director
from app.service.base import BaseService


class DirectorService(BaseService[Director]):
    def __init__(self):
        super().__init__()
        self.dao = DirectorDAO()

    def get_all_directors(self) -> List[Director]:
        return self.dao.get_all_items()

    def get_director(self, did: int) -> Director:
        return self.dao.get_one_by_id(did)
