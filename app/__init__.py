from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# application factory
def create_app(config):
    # create application instance
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    return app
