from flask import Flask, render_template
from flask_migrate import Migrate
from flask_login import LoginManager
from jobplus.config import DeployType, preConfig
from jobplus.models import db, User
from jobplus.handlers import blueprints


def create_app(deployType: DeployType) -> Flask:
    app = Flask(__name__, static_folder='./static')
    app.config.from_pyfile(deployType.configPath())
    app.config.update(preConfig)

    registerExtensions(app)
    registerBluePrints(app)
    registerErrorHandlers(app)

    return app


def registerExtensions(app):
    db.init_app(app)
    Migrate(app, db)
    # with app.app_context():
    #     db.drop_all()
    #     db.create_all()
    loginManager = LoginManager()
    loginManager.init_app(app)

    @loginManager.user_loader
    def load_user(user_id):
        return User.first(id=user_id)

    loginManager.login_view = 'front.login'


def registerBluePrints(app: Flask):
    for bp in blueprints:
        app.register_blueprint(bp)


def registerErrorHandlers(app: Flask):
    @app.errorhandler(404)
    def NotFoundAction(error):
        return render_template('error/404.html'), 404

    @app.errorhandler(500)
    def ServerErrorAction(error):
        return render_template('error/500.html'), 500
