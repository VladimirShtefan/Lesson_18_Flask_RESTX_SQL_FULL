from flask_restx import Namespace, Resource

from app.dao.model.director import director_model
from app.dao.model.exceptions import not_found_model
from app.service.director import DirectorService

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.marshal_list_with(director_model, code=200)
    def get(self):
        return DirectorService().get_all_directors(), 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @director_ns.marshal_with(director_model, code=200)
    @director_ns.response(code=404, description='Id not found', model=not_found_model)
    def get(self, did: int):
        return DirectorService().get_director(did), 200
