from flask import Blueprint

co2_blueprint = Blueprint('co2', __name__, url_prefix='/co2')

# import routes
from . import routes
