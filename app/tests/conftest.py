from unittest import mock

import pytest

from app.dao.movie import MovieDAO


@pytest.fixture
def mock_movie_dao():
    with mock.patch.object(MovieDAO, '__init__', lambda self: None):
        movie_dao = MovieDAO()
        yield movie_dao


