from flask import Blueprint, jsonify, Response, stream_with_context
from .models import Target_temp, Safety_caveats
import json
import random
import time
from datetime import datetime

bp = Blueprint("api", __name__)
random.seed()
@bp.route("/target-temperature/get", methods=["GET"])
def get_target_temp():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 65}})

@bp.route("/target-temperature/put", methods=["POST"])
def put_target_temp():
    target_temp = request.json["target_temp"]

    if target_temp > Safety_caveats.mintemp and target_temp < Safety_caveats.maxtemp:
        new_target_temp = Target_temp(targettemp=target_temp)
        db.session.merge(new_target_temp)
        db.session.commit()
        return True
    else:
        return False

@bp.route("/target-temperature/init", methods=["GET"])
def init_target_temp():
    target_temp = 20
    new_target_temp = Target_temp(targettemp=target_temp)
    db.session.add(new_target_temp)
    db.session.commit()
    return True

@bp.route("/boiler-temperature/get", methods=["GET"])
def get_boiler_temp():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 38}})

@bp.route("/boiler-pressure/get", methods=["GET"])
def pressure():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 40}})

@bp.route("/element-status/get", methods=["GET"])
def element():
    return jsonify({'data': {'time': datetime.now().strftime('%H:%M:%S'), 'value': 100}})
