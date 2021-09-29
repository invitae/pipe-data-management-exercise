import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="sqlite:////tmp/test.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    db.init_app(app)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .view import data_api

    @app.route("/", methods=("GET",))
    def hello():
        return "Welcome to the pipeline platform data management app \U0001F44B!"

    app.register_blueprint(data_api)

    with app.app_context():
        db.drop_all()
        db.create_all()

    return app