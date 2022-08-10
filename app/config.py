from app.constants import DATA_BASE_PATH_FOR_DEV, DATA_BASE_PATH_FOR_PROD


class Config(object):
    JSON_AS_ASCII = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {
        'ensure_ascii': False,
    }
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = 'development'
    TEMPLATES_AUTO_RELOAD = 1
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATA_BASE_PATH_FOR_DEV}'


class ProdConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATA_BASE_PATH_FOR_PROD}'
