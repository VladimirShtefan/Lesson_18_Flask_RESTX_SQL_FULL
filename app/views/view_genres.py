from flask_restx import Namespace, Resource


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        return ''


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid: int):
        return ''
