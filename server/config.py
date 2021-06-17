import os

class Config:
    """
    Base config
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI  = os.getenv(
        'DB_URI', "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY=os.getenv('SECRET', "dumb-secret")
    LOGLEVEL=os.getenv('LOGLEVEL', "info").upper()

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = "development"

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    ENV='testing'

class ProductionConfig(Config):
    TESTING = False
    DEBUG = False
    ENV='production'
    LOGLEVEL='error'

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

