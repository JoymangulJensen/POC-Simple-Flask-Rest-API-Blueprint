from flask import Blueprint

# creation of new co2 blueprint with /co2 prefix
co2_blueprint = Blueprint('co2', __name__, url_prefix='/co2')

# import routes
from . import routes
