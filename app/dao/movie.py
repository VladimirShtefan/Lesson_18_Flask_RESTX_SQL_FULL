from typing import List

from app.dao.base import BaseDAO
from app.dao.model.director import Director
from app.dao.model.genre import Genre
from app.dao.model.movie import Movie


class MovieDAO(BaseDAO[Movie]):
    __model__ = Movie

    def get_all_rows(self,
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

    def add_row(self,
                title: str,
                description: str,
                trailer: str,
                year: int,
                rating: float,
                genre_name: str,
                director_name: str
                ) -> Movie:
        director = self._db_session.query(Director).filter(Director.name.ilike(director_name)).first()
        genre = self._db_session.query(Genre).filter(Genre.name.ilike(genre_name)).first()
        if not director:
            director_model = Director(name=director_name)
            self._db_session.add(director_model)
            self._db_session.commit()
            director_id = director_model.id
        else:
            director_id = director.id
        if not genre:
            genre_model = Genre(name=genre_name)
            self._db_session.add(genre_model)
            self._db_session.commit()
            genre_id = genre_model.id
        else:
            genre_id = genre.id

        new_movie = Movie(
            director_id=director_id,
            genre_id=genre_id,
            title=title,
            description=description,
            trailer=trailer,
            year=year,
            rating=rating
        )
        self._db_session.add(new_movie)
        self._db_session.commit()
        return new_movie
