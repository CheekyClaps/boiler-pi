from flask import Blueprint, render_template, request

bp = Blueprint("views", __name__)

@bp.route("/", methods=['GET', 'POST'])
def index():
    target_temperature = request.form.get("target_temperature")
    print(target_temperature)
    return render_template("index.html")

@bp.route("/chart")
def chart():
    return render_template("chart.html")
