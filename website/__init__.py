from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy# as db

# Init SQL Alchemy class
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='sukkel', # Make this gen base64 ?
        SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3',
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
    
    # Init SQL Alchemy app
    db.init_app(app)    

    # init DB file
    from .models import Boiler_temp, Safety_caveats
    with app.app_context():
        db.create_all()

    # Init routes
    from .views import bp
    app.register_blueprint(bp, url_prefix="/")

    from .api import bp
    app.register_blueprint(bp, url_prefix="/api")

    return app
