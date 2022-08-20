from flask_restx import Namespace, Resource

from app.dao.model.exceptions import not_found_model
from app.dao.model.genre import genre_model
from app.service.genre import GenreService

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.marshal_list_with(genre_model, code=200)
    def get(self):
        return GenreService().get_all_genres(), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @genre_ns.marshal_with(genre_model, code=200)
    @genre_ns.response(code=404, description='Id not found', model=not_found_model)
    def get(self, gid: int):
        return GenreService().get_genre(gid), 200
