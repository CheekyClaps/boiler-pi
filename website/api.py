from flask import Blueprint, jsonify
from random import sample

bp = Blueprint("api", __name__)

@bp.route("/temperature")
def temperature():
    return jsonify({'temperature' : sample(range(1,10), 5)}) 

@bp.route("/pressure")
def pressure():
    return jsonify({'pressure' : sample(range(1,10), 5)}) 
