from unittest.mock import MagicMock


class TestMovieDAO:
    def test_get_one_by_id(self, mock_movie_dao):
        mock_db_session = MagicMock()
        mock_db_session.query.return_value.get_or_404.return_value = {'id': 1}

        mock_movie_dao.db_session = mock_db_session

        assert mock_movie_dao.get_one_by_id(1) == {'id': 1}

    def test_get_all_movies(self, mock_movie_dao):
        mock_db_session = MagicMock()
        query = mock_db_session.query
        query.return_value.join.return_value.filter_by.return_value.all.return_value = [
            {"director_name": "Тейлор Шеридан", "pk": 1}
        ]
        query.return_value.all.return_value = [{'id': 1}, {'id': 2}]

        mock_movie_dao.db_session = mock_db_session
        assert mock_movie_dao.get_all_movies() == [{'id': 1}, {'id': 2}]
        assert mock_movie_dao.get_all_movies(director_name='Тейлор Шеридан') == [{"director_name": "Тейлор Шеридан", "pk": 1}]


