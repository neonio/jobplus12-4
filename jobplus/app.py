from flask import Flask
from jobplus.config import DeployType, preConfig


def create_app(deployType: DeployType) -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(deployType.configPath())
    app.config.update(preConfig)

    registerExtensions(app)
    registerBluePrints(app)
    registerErrorHandlers(app)

    return app


def registerExtensions(app: Flask):
    pass


def registerBluePrints(app: Flask):
    pass


def registerErrorHandlers(app: Flask):
    pass
