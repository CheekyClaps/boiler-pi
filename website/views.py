from flask import Blueprint, flash, render_template, request
from . import db
from .models import Boiler_temp, Safety_caveats

bp = Blueprint("views", __name__)

@bp.route("/", methods=['GET', 'POST'])
def index():
    #target_temperature = Boiler_temp.query.get(1)
    new_target_temperature = request.form.get("target_temperature")
    if new_target_temperature and new_target_temperature >= '90':
        flash(new_target_temperature + " is too high!", category='danger')
    elif new_target_temperature and new_target_temperature <= '18':
        flash(new_target_temperature + " is too low!", category='danger')
    #elif target_temperature and new_target_temperature:
    elif new_target_temperature:
        new_set_target_temperature = Boiler_temp(targettemp=new_target_temperature)
        #db.session.update(new_set_target_temperature)
    #else:
     #   new_set_target_temperature = Boiler_temp(targettemp=new_target_temperature)
        print(new_set_target_temperature)
        db.session.add(new_set_target_temperature)
        db.session.commit()

    return render_template("index.html")

@bp.route("/chart")
def chart():
    return render_template("chart.html")
