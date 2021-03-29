from flask import Blueprint

patient_blueprint = Blueprint('patient', __name__, url_prefix='/patients')
experience_blueprint= Blueprint('experience',__name__,url_prefix='/experiences')

# import routes
from . import routes
