import pytest

from app.dao.genre import GenreDAO


@pytest.fixture()
def genre_dao(db):
    return GenreDAO(db.session)
