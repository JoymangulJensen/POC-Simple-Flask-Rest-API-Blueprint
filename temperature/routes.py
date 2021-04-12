# Temperature
from flask import jsonify
from flask_api import status
from temperature import temperature_blueprint
from temperature.models import Temperature


@temperature_blueprint.route('')
def get_temperature():
    temperatures = Temperature.query.all()
    return jsonify(temperatures)

@temperature_blueprint.route("<int:temperature_id>", methods=['GET'])
def get_co2_by_id(temperature_id):
    temperatures = Temperature.query.filter_by(temperature_id=temperature_id).first()
    if temperatures is not None:
        return jsonify(temperatures), status.HTTP_200_OK
    return jsonify(temperatures), status.HTTP_409_CONFLICT
