from typing import List
from sqlalchemy.exc import IntegrityError

from app.dao.base import BaseDAO
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie
from app.exceptions import BadRequest
from logger import create_logger


logger = create_logger(__name__)


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_director_and_genre_id(self, genre_name: str, director_name: str) -> tuple[int, int]:
        director = self._db_session.query(Director).filter(Director.name.ilike(director_name)).first()
        genre = self._db_session.query(Genre).filter(Genre.name.ilike(genre_name)).first()
        if not director:
            director_model = Director(name=director_name)
            self._db_session.add(director_model)
            self._db_session.flush()
            director_id = director_model.id
        else:
            director_id = director.id
        if not genre:
            genre_model = Genre(name=genre_name)
            self._db_session.add(genre_model)
            self._db_session.flush()
            genre_id = genre_model.id
        else:
            genre_id = genre.id
        return director_id, genre_id

    def get_all_movies(self,
                       director_name: str,
                       director_id: int,
                       genre_name: str,
                       genre_id: int,
                       year: int
                       ) -> List[Movie]:

        movie_query = self._db_session.query(Movie)
        if director_name:
            movie_query = movie_query.join(Director).filter(Director.name.ilike(f'%{director_name}%'))
        if genre_name:
            movie_query = movie_query.join(Genre).filter(Genre.name.ilike(f'%{genre_name}%'))
        if year:
            movie_query = movie_query.filter(Movie.year == year)
        if director_id:
            movie_query = movie_query.filter(Movie.director_id == director_id)
        if genre_id:
            movie_query = movie_query.filter(Movie.genre_id == genre_id)
        return movie_query.all()

    def add_movie(self, genre_name: str, director_name: str, **kwargs) -> Movie:
        director_id, genre_id = self.get_director_and_genre_id(genre_name=genre_name, director_name=director_name)
        data = {'director_id': director_id, 'genre_id': genre_id}
        data.update(kwargs)

        new_movie = Movie(**data)

        self._db_session.add(new_movie)
        try:
            self._db_session.flush()
        except IntegrityError as e:
            self._db_session.rollback()
            logger.info(e.orig)
            raise BadRequest(e.orig)
        else:
            return new_movie

    def put_movie(self, id: int, genre_name: str, director_name: str, **kwargs):
        director_id, genre_id = self.get_director_and_genre_id(genre_name=genre_name, director_name=director_name)
        data = {'director_id': director_id, 'genre_id': genre_id}
        data.update(kwargs)
        try:
            self._db_session.query(Movie).filter_by(id=id).update(data)
        except IntegrityError as e:
            self._db_session.rollback()
            logger.info(e.orig)
            raise BadRequest(e.orig)
