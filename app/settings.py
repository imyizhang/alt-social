import os


class Config:

    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", "secret-key")


class DevelopmentConfig(Config):

    DEBUG = True


class TestingConfig(Config):

    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
