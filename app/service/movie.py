from typing import List

from app.dao.model.movie import Movie
from app.dao.movie import MovieDAO
from app.service.base import BaseService


class MovieService(BaseService[Movie]):
    def __init__(self):
        super().__init__()
        self.dao = MovieDAO()

    @staticmethod
    def get_director_and_genre_id(**kwargs):
        title = kwargs.get('title')
        description = kwargs.get('description')
        trailer = kwargs.get('trailer')
        year = kwargs.get('year')
        rating = kwargs.get('rating')
        genre_name = kwargs.get('genre_name')
        director_name = kwargs.get('director_name')
        return {'title': title,
                'description': description,
                'trailer': trailer,
                'year': year,
                'rating': rating,
                'genre_name': genre_name,
                'director_name': director_name
                }

    def get_movies(self, **kwargs) -> List[Movie]:
        director_name = kwargs.get('director_name')
        director_id = kwargs.get('director_id')
        genre_name = kwargs.get('genre_name')
        genre_id = kwargs.get('genre_id')
        year = kwargs.get('year')
        return self.dao.get_all_movies(director_name, director_id, genre_name, genre_id, year)

    def add_movie(self, **kwargs) -> Movie:
        items = self.get_director_and_genre_id(**kwargs)
        return self.dao.add_movie(**items)

    def put_movie(self, id: int, **kwargs):
        items = self.get_director_and_genre_id(**kwargs)
        return self.dao.put_movie(id=id, **items)

    def delete_movie(self, id: int):
        return self.dao.delete_row(id=id)

    def get_movie(self, id: int):
        return self.dao.get_one_by_id(id=id)
