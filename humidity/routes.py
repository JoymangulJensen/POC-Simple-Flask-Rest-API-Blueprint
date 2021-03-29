# Pressure
from flask import jsonify
from flask_api import status

from humidity import humidity_blueprint
from humidity.models import Humidity


@humidity_blueprint.route('')
def get_humiditys():
    pressures = Humidity.query.all()
    return jsonify(pressures), status.HTTP_200_OK