from flask_restx import Resource, Namespace


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return ''

    def post(self):
        return ''


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        return ''

    def put(self, mid: int):
        return ''

    def patch(self, mid: int):
        return ''

    def delete(self, mid: int):
        return ''
