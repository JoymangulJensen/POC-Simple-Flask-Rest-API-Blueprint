from flask import Blueprint

humidity_blueprint = Blueprint('humidity', __name__, url_prefix='/humidity')

# import routes
from . import routes
