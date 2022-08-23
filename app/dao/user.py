from app.dao.base import BaseDAO
from app.dao.model.user import User
from sqlalchemy.exc import IntegrityError

from app.exceptions import BadRequest
from logger import create_logger

logger = create_logger(__name__)


class UserDAO(BaseDAO[User]):
    __model__ = User

    def create_user(self, username: str, password: bytes, role: str):
        new_user = User(username=username, password=password, role=role)
        self._db_session.add(new_user)
        try:
            self._db_session.flush()
        except IntegrityError as e:
            self._db_session.rollback()
            logger.info(e.orig)
            raise BadRequest(e.orig)

    def search_user(self, username: str) -> User | None:
        user = self._db_session.query(User).filter_by(username=username).first()
        return user

    def add_user_token(self, user: User, refresh_token: str):
        user.refresh_token = refresh_token
        self._db_session.flush()
