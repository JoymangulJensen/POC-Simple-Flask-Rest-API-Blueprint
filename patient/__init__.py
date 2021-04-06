from flask import Blueprint

patient_blueprint = Blueprint('patient', __name__, url_prefix='/patients')

# import routes
from . import routes
