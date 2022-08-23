from flask_restx import Namespace, Resource

from app.dao.model.user import user_model
from app.service.parsers import user_parser
from app.service.user import UserService

user_ns = Namespace('auth')


@user_ns.route('/')
class UserView(Resource):
    # @user_ns.expect(user_parser)
    # @user_ns.marshal_list_with(movie_model, code=200)
    def put(self):
    #     data = movie_filter_parser.parse_args()
    #     return MovieService().get_movies(**data), 200
        pass

    @user_ns.expect(user_parser)
    @user_ns.marshal_list_with(user_model, code=201, description='Created')
    # @movie_ns.response(code=400, description='Bad request', model=bad_request_model)
    def post(self):
        data = user_parser.parse_args()
        request = UserService().search_user(**data)

        # return request, 201, {'Location': url_for('movies_movie_view', mid=request.id)}
        return ""
