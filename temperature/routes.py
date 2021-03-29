# Temperature
from flask import jsonify

from temperature import temperature_blueprint
from temperature.models import Temperature


@temperature_blueprint.route('')
def get_temperature():
    temperatures = Temperature.query.all()
    return jsonify(temperatures)