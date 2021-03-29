from dataclasses import dataclass
import datetime
from app import db


@dataclass
class Humidity(db.Model):
    __tablename__ = 'Humidity'

    humidity_id: int
    humidity_lib: str
    value: float
    unity: str
    measure_date:  datetime.date
    measure_time:  datetime.time
    creation_date: datetime.date
    creation_time: datetime.time


    humidity_id = db.Column(db.Integer(), primary_key=True)
    humidity_lib = db.Column(db.String())
    value = db.Column(db.Float())
    unity = db.Column(db.String())
    measure_date = db.Column(db.Date())
    measure_time = db.Column(db.Time())
    creation_date = db.Column(db.Date())
    creation_time = db.Column(db.Time())
