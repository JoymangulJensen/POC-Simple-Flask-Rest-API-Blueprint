from flask import Blueprint

temperature_blueprint = Blueprint('temperature', __name__, url_prefix='/temperature')

# import routes
from . import routes
