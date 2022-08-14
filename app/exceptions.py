class BaseAppException(Exception):
    code = 500
    message = 'Что то пошло не так'


class MovieNotFound(BaseAppException):
    code = 404
    message = 'Фильм с текущим id не найден'
