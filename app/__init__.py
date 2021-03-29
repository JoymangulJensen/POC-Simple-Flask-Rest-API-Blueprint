from app.utils import CustomJSONEncoder
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

db = SQLAlchemy()
mongo = PyMongo()

# application factory
def create_app(config):
    # create application instance
    app = Flask(__name__)
    app.config.from_object(config)
    app.json_encoder = CustomJSONEncoder

    
    
    db.init_app(app)
    
    from noise import noise_blueprint
    from co2 import co2_blueprint
    from humidity import humidity_blueprint
    from patient import patient_blueprint, experience_blueprint
    from temperature import temperature_blueprint

   
    app.register_blueprint(temperature_blueprint)
    app.register_blueprint(humidity_blueprint)
    app.register_blueprint(noise_blueprint)
    app.register_blueprint(patient_blueprint)
    app.register_blueprint(experience_blueprint)
    app.register_blueprint(co2_blueprint)
    
    return app
