from flask import Blueprint

noise_blueprint = Blueprint('humidity', __name__, url_prefix='/humidity')

# import routes
from . import routes
