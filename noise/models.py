from dataclasses import dataclass
import datetime
from app import db


@dataclass
class Noise(db.Model):
    __tablename__ = 'Noise'

    noise_id: int
    noise_lib: str
    value: float
    unity: str
    measure_date:  datetime.date
    measure_time:  datetime.time

    noise_id = db.Column(db.Integer(), primary_key=True)
    noise_lib = db.Column(db.String())
    value = db.Column(db.Float())
    unity = db.Column(db.String())
    measure_date = db.Column(db.Date())
    measure_time = db.Column(db.Time())