from flask import Blueprint, render_template

bp = Blueprint("views", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/chart")
def chart():
    return render_template("chart.html")
