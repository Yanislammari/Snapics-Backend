from flask import Flask
from src.utils.config import db
from src.utils.config.config import Config
from src.controllers.user_controller import user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(user_blueprint)

    with app.app_context():
        db.create_all()

    return app
