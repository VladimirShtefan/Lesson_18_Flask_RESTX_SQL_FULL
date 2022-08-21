from flask_restx import Namespace, Resource

from app.dao.model.exceptions import not_found_model, bad_request_model
from app.dao.model.genre import genre_model
from app.service.genre import GenreService
from app.service.parsers import name_model_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.marshal_list_with(genre_model, code=200)
    def get(self):
        return GenreService().get_all_items(), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @genre_ns.marshal_with(genre_model, code=200)
    @genre_ns.response(code=404, description='Id not found', model=not_found_model)
    def get(self, gid: int):
        return GenreService().get_item_by_id(gid), 200

    @genre_ns.expect(name_model_parser)
    @genre_ns.response(code=204, description='Updated')
    @genre_ns.response(code=404, description='Id not found', model=not_found_model)
    @genre_ns.response(code=400, description='Bad request', model=bad_request_model)
    def put(self, gid: int):
        data = name_model_parser.parse_args()
        GenreService().put_genre(gid, **data)
        return "", 204

    def delete(self, gid: int):
        pass
