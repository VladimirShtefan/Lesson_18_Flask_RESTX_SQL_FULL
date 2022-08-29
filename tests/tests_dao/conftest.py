import pytest

from app.dao.movie import MovieDAO


@pytest.fixture()
def movie_dao(app_with_db):
    return MovieDAO(app_with_db.session)
