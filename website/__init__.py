from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Init SQL Alchemy
db = SQLAlchemy()
db_name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='sukkel', # Make this gen base64 ?
        SQLALCHEMY_DATABASE_URI="sqlite:///" + db_name,
        #SQLALCHEMY_DATABASE_URI=path.join(app.instance_path, 'website.' + db_name),
    )
    
    # Init DB
    db.init_app(app)
    from .models import Boiler_temp, Safety_caveats
    create_db(app)

    # Init routes
    from .views import bp
    app.register_blueprint(bp, url_prefix="/")

    from .api import bp
    app.register_blueprint(bp, url_prefix="/api")

    return app

# Create if not exists database file .db
def create_db(app):
    if not path.exists("website/" + db_name):
        db.create_all(app=app)
        print("DB CREATED")
