from flask import Blueprint, flash, render_template, request
from .models import Target_temp, Safety_caveats
import subprocess
from . import db

# Init flask blueprint
bp = Blueprint("views", __name__)

# Get server ip for api calls
server_ip = subprocess.Popen("sudo hostname -I", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

@bp.route("/", methods=['GET'])
def index(ip=server_ip):
    return render_template("index.html", server_ip=ip)

@bp.route("/boiler-control", methods=['GET', 'POST'])
def chart(ip=server_ip):

    new_target_temperature = request.form.get("target_temperature")
    new_heating_time = request.form.get("heating_time")
 
    if new_heating_time and new_heating_time > '0' and new_target_temperature:
        flash("Cannot set both!", category='danger')
    elif new_heating_time and new_heating_time > '0':
        print(new_heating_time)
    elif new_target_temperature and new_target_temperature >= '90':
        flash(new_target_temperature + " is too high!", category='danger')
    elif new_target_temperature and new_target_temperature <= '18':
        flash(new_target_temperature + " is too low!", category='danger')
    elif new_target_temperature:
        print(new_target_temperature)

    return render_template("boiler-control.html", server_ip=ip)

@bp.route("/timer", methods=["GET"])
def timer():
    try:
        output = subprocess.check_output("python3 website/controller/timer.py", shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    return render_template("index.html", **locals())
