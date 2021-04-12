# Pressure
from flask import jsonify
from flask_api import status
from flask_api import status
from humidity import humidity_blueprint
from humidity.models import Humidity


@humidity_blueprint.route('')
def get_humidities():
    pressures = Humidity.query.all()
    return jsonify(pressures), status.HTTP_200_OK

@humidity_blueprint.route("<int:humidity_id>", methods=['GET'])
def get_co2_by_id(humidity_id):
    humidity = Humidity.query.filter_by(humidity_id=humidity_id).first()
    if humidity is not None:
        return jsonify(humidity), status.HTTP_200_OK
    return jsonify(humidity), status.HTTP_409_CONFLICT