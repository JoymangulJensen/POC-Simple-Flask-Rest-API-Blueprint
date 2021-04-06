from flask import jsonify,request
from flask_api import status

from patient import patient_blueprint
from patient.models import Patient, PatientExperience

from app import db
from sqlalchemy.orm import joinedload


@patient_blueprint.route('')
def get_patients():
    patients = Patient.query.all()
    return jsonify(patients), status.HTTP_200_OK

@patient_blueprint.route('/<int:id>')
def get_patient(id):
    try:
        patient=Patient.query.get(id)
        return jsonify(patient), status.HTTP_200_OK
    except:
        return status.HTTP_404_NOT_FOUND
