from dataclasses import dataclass
import datetime
from app import db


@dataclass
class Temperature(db.Model):
    __tablename__ = 'Temperature'
    
    temperature_id :int
    temperature_lib: str
    value: float
    unity: str
    min_temp_lib: str
    min_temp:  float
    date_min_temp: datetime.date
    time_min_temp: datetime.time
    max_temp_lib : str
    max_temp : float
    date_max_temp: datetime.date
    time_max_temp: datetime.time
    measure_date: datetime.date
    measure_time: datetime.time


    temperature_id = db.Column(db.Integer, primary_key=True)
    temperature_lib = db.Column(db.String(80))
    value = db.Column(db.Float())
    unity = db.Column(db.String(80))
    min_temp_lib = db.Column(db.String())
    min_temp = db.Column(db.Float())
    date_min_temp = db.Column(db.Date())
    time_min_temp = db.Column(db.Time())
    max_temp_lib = db.Column(db.String(80))
    max_temp = db.Column(db.Float())
    date_max_temp = db.Column(db.Date())
    time_max_temp = db.Column(db.Time())
    measure_date = db.Column(db.Date())
    measure_time = db.Column(db.Time())



