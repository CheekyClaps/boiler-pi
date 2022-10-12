from . import db
#from flask_sqlalchemy import SQLAlchemy

class Boiler_temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    targettemp = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.targettemp})'

class Safety_caveats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mintemp = db.Column(db.Integer, nullable=False)
    maxtemp = db.Column(db.Integer, nullable=False)
    minpressure = db.Column(db.Integer, nullable=False)
    maxpressure = db.Column(db.Integer, nullable=False)
