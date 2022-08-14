from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.service.base import BaseService


class MovieService(BaseService[Movie]):
    def __init__(self):
        super().__init__()
        self.dao = MovieDAO()

    def get_movies(self, **kwargs):
        director_name = kwargs.get('director_name')
        director_id = kwargs.get('director_id')
        genre_name = kwargs.get('genre_name')
        genre_id = kwargs.get('genre_id')
        year = kwargs.get('year')
        return self.dao.get_all_rows(director_name, director_id, genre_name, genre_id, year)

    def add_movie(self, **kwargs):
        # return self.dao.add_row(self.dao.__model__(**kwargs))
        title = kwargs.get('title')
        description = kwargs.get('description')
        trailer = kwargs.get('trailer')
        year = kwargs.get('year')
        rating = kwargs.get('rating')
        genre_name = kwargs.get('genre_name')
        director_name = kwargs.get('director_name')
        new_movie = self.dao.add_row(title, description, trailer, year, rating, genre_name, director_name)
        print(new_movie)
        return new_movie
