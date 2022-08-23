from flask_restx import Namespace, Resource
from flask import url_for

from app.dao.model.director import director_model
from app.dao.model.exceptions import not_found_model, bad_request_model
from app.helpers.decorators import user_required
from app.service.director import DirectorService
from app.service.parsers import name_model_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @user_required(['user', 'admin'])
    @director_ns.marshal_list_with(director_model, code=200)
    @director_ns.response(code=401, description='Unauthorized')
    def get(self):
        return DirectorService().get_all_items(), 200

    @user_required(['admin'])
    @director_ns.expect(name_model_parser)
    @director_ns.marshal_list_with(director_model, code=201, description='Created')
    @director_ns.response(code=400, description='Bad request', model=bad_request_model)
    @director_ns.response(code=401, description='Unauthorized')
    def post(self):
        data = name_model_parser.parse_args()
        request = DirectorService().add_director(**data)
        return request, 201, {'Location': url_for('directors_director_view', did=request.id)}


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @user_required(['user', 'admin'])
    @director_ns.marshal_with(director_model, code=200)
    @director_ns.response(code=404, description='Id not found', model=not_found_model)
    @director_ns.response(code=401, description='Unauthorized')
    def get(self, did: int):
        return DirectorService().get_item_by_id(did), 200

    @user_required(['admin'])
    @director_ns.expect(name_model_parser)
    @director_ns.response(code=204, description='Updated')
    @director_ns.response(code=404, description='Id not found', model=not_found_model)
    @director_ns.response(code=400, description='Bad request', model=bad_request_model)
    @director_ns.response(code=401, description='Unauthorized')
    def put(self, did: int):
        data = name_model_parser.parse_args()
        DirectorService().put_director(did, **data)
        return "", 204

    @user_required(['admin'])
    @director_ns.response(code=204, description='Deleted')
    @director_ns.response(code=404, description='Id not found', model=not_found_model)
    @director_ns.response(code=401, description='Unauthorized')
    def delete(self, did: int):
        DirectorService().del_item(did)
        return "", 204
