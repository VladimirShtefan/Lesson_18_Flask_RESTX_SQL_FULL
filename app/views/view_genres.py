from flask_restx import Namespace, Resource
from flask import url_for

from app.dao.model.exceptions import not_found_model, bad_request_model
from app.dao.model.genre import genre_model
from app.helpers.decorators import user_required
from app.service.genre import GenreService
from app.service.parsers import name_model_parser

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @user_required(['user', 'admin'])
    @genre_ns.marshal_list_with(genre_model, code=200)
    @genre_ns.response(code=401, description='Unauthorized')
    def get(self, username: str):
        return GenreService().get_all_items(), 200

    @user_required(['admin'])
    @genre_ns.expect(name_model_parser)
    @genre_ns.marshal_list_with(genre_model, code=201, description='Created')
    @genre_ns.response(code=400, description='Bad request', model=bad_request_model)
    @genre_ns.response(code=401, description='Unauthorized')
    def post(self, username: str):
        data = name_model_parser.parse_args()
        request = GenreService().add_genre(**data)
        return request, 201, {'Location': url_for('genres_genre_view', gid=request.id)}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @user_required(['user', 'admin'])
    @genre_ns.marshal_with(genre_model, code=200)
    @genre_ns.response(code=404, description='Id not found', model=not_found_model)
    @genre_ns.response(code=401, description='Unauthorized')
    def get(self, gid: int, username: str):
        return GenreService().get_item_by_id(gid), 200

    @user_required(['admin'])
    @genre_ns.expect(name_model_parser)
    @genre_ns.response(code=204, description='Updated')
    @genre_ns.response(code=404, description='Id not found', model=not_found_model)
    @genre_ns.response(code=400, description='Bad request', model=bad_request_model)
    @genre_ns.response(code=401, description='Unauthorized')
    def put(self, gid: int, username: str):
        data = name_model_parser.parse_args()
        GenreService().put_genre(gid, **data)
        return "", 204

    @user_required(['admin'])
    @genre_ns.response(code=204, description='Deleted')
    @genre_ns.response(code=404, description='Id not found', model=not_found_model)
    @genre_ns.response(code=401, description='Unauthorized')
    def delete(self, gid: int, username: str):
        GenreService().del_item(gid)
        return "", 204
