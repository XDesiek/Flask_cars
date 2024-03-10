from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Car(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.Integer, db.ForeignKey("user.id") ,nullable  = False)
    model= db.Column(db.String(100), nullable  = False)
    producer= db.Column(db.String(100), nullable  = False)
    production_year = db.Column(db.Integer, nullable  = False)
    horsepower = db.Column(db.Integer, nullable  = False)
    drive= db.Column(db.String(100), nullable  = False)
    fuel= db.Column(db.String(100), nullable  = False)
    color= db.Column(db.String(100), nullable  = False)
    gearbox= db.Column(db.String(100), nullable  = False)


    def __repr__ (self):
        return f"{self.producer} {self.model}"

