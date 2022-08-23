from flask_restx import fields

from app.setup_api import api

bad_request_model = api.model(
    'BadRequest',
    {
        'error': fields.String(example="UNIQUE constraint failed: model.field"),
        'code': fields.String(example=404),
    }
)

not_found_model = api.model(
    'NotFound',
    {
        'error': fields.String(
            example="Id not found. You have requested this URI [/model/99] but did you mean /model/<int:mid>?"
        ),
    }
)

validation_error = api.model(
    'ValidationError',
    {
        'error': fields.String(example="Password has incorrect format."),
    }
)

unauthorized_error = api.model(
    'Unauthorized',
    {
        'error': fields.String(example="Unauthorized"),
    }
)
