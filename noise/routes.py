from flask import jsonify
from flask_api import status
from noise import noise_blueprint
from noise.models import Noise

@noise_blueprint.route('')
def get_noises():
    pressures = Noise.query.all()
    return jsonify(pressures), status.HTTP_200_OK

@noise_blueprint.route("<int:noise_id>", methods=['GET'])
def get_co2_by_id(noise_id):
    noise = Noise.query.filter_by(noise_id=noise_id).first()
    if noise is not None:
        return jsonify(noise), status.HTTP_200_OK
    return jsonify(noise), status.HTTP_409_CONFLICT
