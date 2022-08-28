from unittest.mock import patch

import pytest

from app.dao.model.genre import Genre
from app.service.genre import GenreService


@pytest.fixture
def mock_genre_dao(db):
    with patch('app.service.genre.GenreDAO') as mock:
        yield mock(db.session)


def test_get_genre_success(mock_genre_dao):
    mock_genre_dao.get_one_by_id.return_value = Genre(id=1, genre_name='test_genre')
    genre = GenreService().get_genre(1)
    assert genre.id == 1
    assert genre.genre_name == 'test_genre'

