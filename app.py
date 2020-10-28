import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#from config import password

db_user = "postgres"
db_host = "localhost"
db_port = 5614


engine = create_engine(f'postgres://postgres:Texans4228!@localhost:5614/ETL')

Base = automap_base()
Base.prepare(engine, reflect=True)

census = Base.classes.census
tract = Base.classes.tract
session = Session(engine)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:Texans4228!@localhost:5614/ETL'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False


@app.route("/")
def welcome():

     return (
         f"/api/v1.0/population<br/>"
         f"/api/v1.0/vehicle_rate<br/>"
         f"/api/v1.0/dealership<br/>")



@app.route("/api/v1.0/population")
def pop():
    session = Session(engine)
    results = session.query(census.Total_Population, census.Total_Housing_Units).all()
    
    session.close()

    pop_housing = []
    for result in results:
        row = {}
        row['Total_Population'] = int(result[0])
        row['Total_Housing_Units'] = int(result[1])
        pop_housing.append(row)

    return jsonify(pop_housing)


@app.route("/api/v1.0/vehicle_rate")
def vehicle():
    session = Session(engine)
    results = session.query(census.Total_Housing_Units, census.Units_Without_Vehicle).all()

    session.close()

    census_list = []
    for result in results:
        row = {}
        row['Total_Housing_Units'] = int(result[0])
        row['Units_Without_Vehicle'] = int(result[1])
        census_list.append(row)
    return jsonify(census_list)

@app.route("/api/v1.0/dealership")
def dealership():
    session = Session(engine)
    results = session.query(tract.Latitude, tract.Longitude, census.Car_Dealer).all()

    session.close()

    dealer_list = []
    for result in results:
        row = {}
        row['Car Dealer'] = result[0]
        row['Latitude'] = float(result[1])
        row['Longitude'] = float(result[2])
        dealer_list.append(row)

    return jsonify(dealer_list)


if __name__ == "__main__":
    app.run(debug=True)