from flask_restx import Namespace, Resource

from app.dao.model.exceptions import unauthorized_error
from app.dao.model.user import token_model
from app.service.parsers import login_parser
from app.service.user import UserService

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    @auth_ns.expect(login_parser)
    @auth_ns.marshal_list_with(token_model, code=201, description='Tokens created')
    @auth_ns.response(code=401, description='Unauthorized', model=unauthorized_error)
    def post(self):
        data = login_parser.parse_args()
        tokens = UserService().search_user(**data)
        return tokens, 201


