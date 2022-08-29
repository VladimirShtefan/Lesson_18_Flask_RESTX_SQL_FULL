import pytest

from werkzeug.exceptions import NotFound


class TestMovieDAO:
    def test_get_all_movies(self, movie_dao):
        isinstance(movie_dao.get_all_movies(), list)
        assert movie_dao.get_all_movies()[0].year == 2018
        assert movie_dao.get_all_movies()[1].year == 2015

    def test_get_one_movie_exception_404(self, movie_dao):
        with pytest.raises(NotFound, match='Id not found'):
            movie_dao.get_one_by_id(999)
