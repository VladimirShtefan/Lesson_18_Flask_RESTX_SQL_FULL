import pytest

from app.dao.model.genre import Genre


@pytest.fixture
def create_genre(db):
    def _wrapper(name: str):
        _genre = Genre(genre_name=name)
        db.session.add(_genre)
        db.session.commit()

    return _wrapper


def test_get_one_genre_success(client, create_genre):
    create_genre('test_genre')

    response = client.get('/genres/1')
    assert response.status_code == 200
    assert response.json == {
        'pk': 1,
        'genre_name': 'test_genre',
    }


def test_get_many_genres_success(client, create_genre):
    for i in range(2):
        create_genre(f'test_genre_{i}')

    response = client.get('/genres/')
    assert response.status_code == 200
    assert response.json == [
        {
            'pk': 1,
            'genre_name': 'test_genre_0',
        },
        {
            'pk': 2,
            'genre_name': 'test_genre_1',
        },
    ]


def test_get_genre_not_found(client):
    response = client.get('/genres/1')
    assert response.status_code == 404
