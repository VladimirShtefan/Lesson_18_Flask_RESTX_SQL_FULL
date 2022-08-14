from flask_restx import Resource, Namespace

from app.dao.model.movie import movie_model
from app.service.movie import MovieService
from app.service.parsers import movie_filter_parser, movie_model_parser

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @movie_ns.expect(movie_filter_parser)
    @movie_ns.marshal_list_with(movie_model, code=200)
    def get(self):
        data = movie_filter_parser.parse_args()
        return MovieService().get_movies(**data), 200

    @movie_ns.expect(movie_model_parser)
    @movie_ns.marshal_list_with(movie_model, code=201, description='Created')
    @movie_ns.response(code=400, description='Bad request')
    def post(self):
        data = movie_model_parser.parse_args()
        return MovieService().add_movie(**data), 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @movie_ns.marshal_with(movie_model, code=200)
    @movie_ns.response(code=404, description='Id not found')
    def get(self, mid: int):
        return MovieService().get_item_by_id(mid), 200

    def put(self, mid: int):
        return ''

    def patch(self, mid: int):
        return ''

    @movie_ns.response(code=204, description='Deleted')
    def delete(self, mid: int):
        MovieService().del_item(mid)
        return None, 204
