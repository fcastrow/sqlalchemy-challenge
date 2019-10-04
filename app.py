#import the usual suspects
#%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt

#import Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#populate data frames
results = session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
stations_df = pd.DataFrame(results, columns=['id', 'station', 'name', 'latitude', 'longitude', 'elevation'])

results = session.query(Measurement.id, Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs).all()
measurements_df = pd.DataFrame(results, columns=['id', 'station', 'date', 'prcp', 'tobs'])

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
# list available routes
    return "Routes:<hr>/api/v1.0/precipatation<br>/api/v1.0/stations<br>/api/v1.0/tobs<br>/api/v1.0/start_date<br>/api/v1.0/start_date/end_date"

@app.route("/api/v1.0/precipatation")
def precipatation():
    d = {}
    for i in measurements_df['id']:
        i -= 1
        d[i] = {
                'id': int(measurements_df['id'][i]),
                'station': measurements_df['station'][i],
                'date': measurements_df['date'][i],
                'prcp': measurements_df['prcp'][i],
                'tobs': measurements_df['tobs'][i]
        }
    return jsonify(d)

@app.route("/api/v1.0/stations")
def stations():
    d = {}
    for i in stations_df['id']:
        i -= 1
        d[i] = {
                'id': int(stations_df['id'][i]),
                'station': stations_df['station'][i],
                'name': stations_df['name'][i],
                'latitude': stations_df['latitude'][i],
                'longitude': stations_df['longitude'][i],
                'elevation': stations_df['elevation'][i]
        }
    return jsonify(d)

@app.route("/api/v1.0/tobs")
def tobs():
    return "tobs"

@app.route("/api/v1.0/<start>")
def start():
    return "start"

@app.route("/api/v1.0/<start>/<end>")
def start_end():
    return "start_end"

if __name__ == "__main__":
    app.run(debug=True)
