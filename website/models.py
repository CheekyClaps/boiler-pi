from . import db

class Target_temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    targettemp = db.Column(db.Integer, nullable=False)

class Safety_caveats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mintemp = db.Column(db.Integer, nullable=False)
    maxtemp = db.Column(db.Integer, nullable=False)
    minpressure = db.Column(db.Integer, nullable=False)
    maxpressure = db.Column(db.Integer, nullable=False)
