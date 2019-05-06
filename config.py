import os

from instance.config import secrete_key, database_uri, test_database_uri

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = secrete_key
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @ staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = test_database_uri


class ProductionConfig(Config):
    pass


config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,
          'default': DevelopmentConfig}
