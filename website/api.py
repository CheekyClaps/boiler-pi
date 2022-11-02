from flask import Blueprint, jsonify, Response
from flask_cors import cross_origin
from w1thermsensor import W1ThermSensor
from datetime import datetime
from .models import Target_temp, Safety_caveats
from . import db

# Init flask blueprint, one wire thermsensor
bp = Blueprint("api", __name__)
thermsensor = W1ThermSensor()

@bp.route("/target-temperature/get", methods=["GET"])
@cross_origin()
def get_target_temp():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 60 }})

@bp.route("/target-temperature/<int:target_temp>", methods=["GET"])
@cross_origin()
def put_target_temp(target_temp):
    # Get safety caveats by id
    safety = Safety_caveats.query.get(1)
    if target_temp > safety.mintemp and target_temp < safety.maxtemp:
        new_target_temp = Target_temp(targettemp=target_temp)
        db.session.merge(new_target_temp)
        db.session.commit()
        return " ", 200
    else:
        return " ", 500

@bp.route("/init", methods=["GET"])
def init_target_temp():
    min_temp = 10
    max_temp = 90
    min_pressure = 20
    max_pressure = 50
    target_temp = 20
    new_safety_caveats = Safety_caveats(mintemp=min_temp, maxtemp=max_temp, minpressure=min_pressure, maxpressure=max_pressure)
    new_target_temp = Target_temp(targettemp=target_temp)
    db.session.add(new_target_temp)
    db.session.add(new_safety_caveats)
    db.session.commit()
    return " ", 200

@bp.route("/boiler-temperature/get", methods=["GET"])
@cross_origin()
def get_boiler_temp():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': thermsensor.get_temperature()}})

@bp.route("/boiler-pressure/get", methods=["GET"])
@cross_origin()
def pressure():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 60}})

@bp.route("/element-status/get", methods=["GET"])
@cross_origin()
def element():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 100}})
