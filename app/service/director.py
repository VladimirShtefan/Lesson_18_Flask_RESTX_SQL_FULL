from typing import List

from app.dao.director import DirectorDAO
from app.dao.model.director import Director
from app.service.base import BaseService


class DirectorService(BaseService[Director]):
    def __init__(self):
        super().__init__()
        self.dao = DirectorDAO()

    def put_director(self, did: int, **kwargs):
        return self.dao.put_director(did, **kwargs)
