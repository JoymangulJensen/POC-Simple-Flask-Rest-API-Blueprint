from flask import jsonify,request
from flask_api import status

from patient import patient_blueprint,experience_blueprint
from patient.models import Patient, PatientExperience

from app import db


@patient_blueprint.route('')
def get_patients():
    patients = Patient.query.all()
    return jsonify(patients), status.HTTP_200_OK

@patient_blueprint.route('/<int:id>')
def get_patient(id):
    patient=Patient.query.get(id)
    return jsonify(patient), status.HTTP_200_OK



@experience_blueprint.route('')
def get_experiences():
    experiences=PatientExperience.query.all()
    return jsonify(experiences), status.HTTP_200_OK

@experience_blueprint.route('/<int:id>')
def get_patient_experience(id):
    ex = PatientExperience.query.join(Patient, PatientExperience.trc_patient_id==Patient.trc_patient_id)
    return jsonify(ex), status.HTTP_200_OK
