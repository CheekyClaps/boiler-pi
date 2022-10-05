from flask import Blueprint, jsonify, Response, stream_with_context
import json
import random
import time
from datetime import datetime


bp = Blueprint("api", __name__)
random.seed()

@bp.route("/target-temperature")
def target():
    def target_temp():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': 60})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(target_temp()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response


@bp.route("/temperature")
def temperature():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': random.random() * 50})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response



@bp.route("/pressure")
def pressure():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': 40})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@bp.route("/element-status")
def element():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': 10})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response
