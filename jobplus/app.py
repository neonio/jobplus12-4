from flask import Flask
from jobplus.config import DeployType, preConfig
from jobplus.models import db


def create_app(deployType: DeployType) -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(deployType.configPath())
    app.config.update(preConfig)

    registerExtensions(app)
    registerBluePrints(app)
    registerErrorHandlers(app)

    return app


def registerExtensions(app: Flask):
    db.init_app(app)
    with app.app_context():
        db.drop_all()
        db.create_all()


def registerBluePrints(app: Flask):
    pass


def registerErrorHandlers(app: Flask):
    pass
