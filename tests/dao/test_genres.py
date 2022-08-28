import random

import pytest
from werkzeug.exceptions import NotFound

from app.dao.model.genre import Genre


@pytest.fixture
def genre(db):
    _genre = Genre(genre_name='test_genre')
    db.session.add(_genre)
    db.session.commit()
    return _genre


def test_get_one_genre_success(genre_dao, genre):
    _genre = genre_dao.get_one_by_id(genre.id)
    assert _genre.id == 1
    assert _genre.genre_name == 'test_genre'


def test_get_one_genre_not_exists(genre_dao):
    with pytest.raises(NotFound, match='Id not found'):
        genre_dao.get_one_by_id(random.randint(0, 100))


def test_get_all_genres(genre_dao, genre):
    genres = genre_dao.get_all_items()
    assert isinstance(genres, list)
    assert len(genres) == 1
    assert isinstance(genres[0], Genre)
    assert genres[0] == genre
