from flask import Blueprint

noise_blueprint = Blueprint('noise', __name__, url_prefix='/noise')

# import routes

from . import routes