# CO2
from flask import jsonify
from flask_api import status

# import co2 blueprint and Co2 model
from co2 import co2_blueprint
from co2.models import Co2

# retreive all co2's data 
@co2_blueprint.route('')
def get_co2s():
    co2s = Co2.query.all()
    return jsonify(co2s), status.HTTP_200_OK

# get co2 data by co2 id
@co2_blueprint.route("<int:co2_id>", methods=['GET'])
def get_co2_by_id(co2_id):
    co2 = Co2.query.filter_by(co2_id=co2_id).first()
    if co2 is not None:
        return jsonify(co2), status.HTTP_200_OK
    return jsonify(co2), status.HTTP_409_CONFLICT
