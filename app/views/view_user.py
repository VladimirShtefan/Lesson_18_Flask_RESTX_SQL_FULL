from flask_restx import Namespace, Resource

from app.dao.model.exceptions import validation_error, bad_request_model
from app.dao.model.user import user_model
from app.service.parsers import user_parser
from app.service.user import UserService

user_ns = Namespace('users')


@user_ns.route('/')
class UserView(Resource):
    @user_ns.expect(user_parser)
    @user_ns.marshal_list_with(user_model, code=201, description='Created')
    @user_ns.response(code=200, description='Password incorrect format.', model=validation_error)
    @user_ns.response(code=400, description='Bad request', model=bad_request_model)
    def post(self):
        data = user_parser.parse_args()
        UserService().create_user(**data)
        return "", 201
