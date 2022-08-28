class TestMovieDAO:
    sample_movie = {
            "title": "Test",
            "description": "Test",
            "trailer": "Test",
            "year": 2022,
            "rating": 1,
            "genre_name": 'Test',
            "director_name": 'Test',
    }

    def test_get_movies(self, movie_dao):
        all_movies = movie_dao.get_all_movies()
        assert isinstance(all_movies, list)
        assert all_movies[1].year == 2015
        assert len(all_movies) > 1

    def test_add_movie(self, movie_dao):
        new_movie = movie_dao.add_movie(**self.sample_movie)
        assert new_movie.id == 21
        assert new_movie.genre_id == 19
