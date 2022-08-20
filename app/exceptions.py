class BaseAppException(Exception):
    def __init__(self, message: str):
        self.message = message
    code = 500


class NotFound(BaseAppException):
    code = 404


class BadRequest(BaseAppException):
    code = 400
