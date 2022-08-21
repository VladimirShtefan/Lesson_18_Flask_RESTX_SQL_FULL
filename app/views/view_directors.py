from flask_restx import Namespace, Resource

from app.dao.model.director import director_model
from app.dao.model.exceptions import not_found_model, bad_request_model
from app.service.director import DirectorService
from app.service.parsers import name_model_parser

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.marshal_list_with(director_model, code=200)
    def get(self):
        return DirectorService().get_all_items(), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @director_ns.marshal_with(director_model, code=200)
    @director_ns.response(code=404, description='Id not found', model=not_found_model)
    def get(self, did: int):
        return DirectorService().get_item_by_id(did), 200

    @director_ns.expect(name_model_parser)
    @director_ns.response(code=204, description='Updated')
    @director_ns.response(code=404, description='Id not found', model=not_found_model)
    @director_ns.response(code=400, description='Bad request', model=bad_request_model)
    def put(self, did: int):
        data = name_model_parser.parse_args()
        DirectorService().put_director(did, **data)
        return "", 204

    def delete(self, did: int):
        pass
