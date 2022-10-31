from flask import Blueprint, flash, render_template, request
from .models import Target_temp, Safety_caveats
from . import db

bp = Blueprint("views", __name__)

@bp.route("/", methods=['GET', 'POST'])
def index():
    new_target_temperature = request.form.get("target_temperature")
    if new_target_temperature and new_target_temperature >= '90':
        flash(new_target_temperature + " is too high!", category='danger')
    elif new_target_temperature and new_target_temperature <= '18':
        flash(new_target_temperature + " is too low!", category='danger')
    elif new_target_temperature:
        print(new_target_temperature)

    return render_template("index.html", server_ip=request.environ)

@bp.route("/chart")
def chart():
    return render_template("chart.html")
