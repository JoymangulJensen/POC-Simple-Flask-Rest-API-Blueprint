from dataclasses import dataclass
import datetime
from app import db

@dataclass
class PatientExperience(db.Model):
    __tablename__='patient_experience'
    experience_id:int
    start_date: datetime.date
    end_date = datetime.date
    created_at: datetime.date
    updated_at: datetime.date
    trc_patient_id:int

    
    experience_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date(),nullable=True)
    end_date = db.Column(db.Date(),nullable=True)
    created_at = db.Column("createdAt",db.Date(),nullable=True)
    updated_at = db.Column("updatedAt",db.Date(),nullable=True)
    trc_patient_id=db.Column(db.Integer(), db.ForeignKey('patient.TRC_patient_id'))


@dataclass
class Patient(db.Model):
    __tablename__ = 'patient'

    trc_patient_id:int
    name: str
    surname: str
    address: str
    birthday: str
    trc_traitement_id: int
    trc_rendered_traitement_id: int
    lmd_patient_id: int
    created_at: datetime.date
    updated_at: datetime.date
    experiences: PatientExperience
    

    trc_patient_id = db.Column("TRC_patient_id",db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    address= db.Column("adress",db.Text(), nullable=True)
    birthday= db.Column(db.String(250), nullable=True)
    trc_traitement_id=db.Column("TRC_traitement_id",db.Integer)
    trc_rendered_traitement_id=db.Column("TRC_rendered_traitement_id",db.Integer)
    lmd_patient_id=db.Column("LMD_patient_id",db.Integer)
    created_at = db.Column("createdAt",db.Date,nullable=True)
    updated_at = db.Column("updatedAt",db.Date,nullable=True)
    experiences =  db.relationship('PatientExperience', backref = 'patient')
   