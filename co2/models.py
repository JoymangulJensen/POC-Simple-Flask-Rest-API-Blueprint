from dataclasses import dataclass
import datetime
from app import db

# our Co2 model 
@dataclass
class Co2(db.Model):
    __tablename__ = 'co2'
# attributes of Co2 model
    co2_id: int
    co2_lib: str
    value: float
    unity: str
    measure_date:  datetime.date
    measure_time:  datetime.time
    creation_date:  datetime.date
    creation_time:  datetime.time
    experience_id: int
    materiel_id: int
# mapping Class Co2 and table co2
    co2_id = db.Column(db.Integer(), primary_key=True)
    co2_lib = db.Column(db.String())
    value = db.Column(db.Float())
    unity = db.Column(db.String())
    measure_date = db.Column(db.Date())
    measure_time = db.Column(db.Time())
    creation_date = db.Column(db.Date())
    creation_time = db.Column(db.Time())
    experience_id = db.Column(db.Integer())
    materiel_id = db.Column(db.Integer())
