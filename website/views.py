from flask import Blueprint, flash, render_template, request
from .models import Target_temp, Safety_caveats
import subprocess
from . import db

# Init flask blueprint
bp = Blueprint("views", __name__)

# Get server ip for api calls
# server_ip = subprocess.Popen("ipconfig getifaddr en0", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()
server_ip = subprocess.Popen("hostname -I", shell=True,stdout=subprocess.PIPE).communicate()[0].decode('utf-8').strip()

@bp.route("/", methods=['GET', 'POST'])
def index(ip=server_ip):
    new_target_temperature = request.form.get("target_temperature")
    if new_target_temperature and new_target_temperature >= '90':
        flash(new_target_temperature + " is too high!", category='danger')
    elif new_target_temperature and new_target_temperature <= '18':
        flash(new_target_temperature + " is too low!", category='danger')
    elif new_target_temperature:
        print(new_target_temperature)

    return render_template("index.html", server_ip=ip)

@bp.route("/chart")
def chart():
    return render_template("chart.html")
