# Pressure
from flask import jsonify
from flask_api import status

from noise import noise_blueprint
from noise.models import Noise


@noise_blueprint.route('')
def get_noises():
    pressures = Noise.query.all()
    return jsonify(pressures), status.HTTP_200_OK