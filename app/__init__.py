from flask import Flask

from .routes import main
from .settings import config


def create_app(environment):

    app = Flask(__name__)
    app.config.from_object(config[environment])
    app.register_blueprint(main)

    return app
