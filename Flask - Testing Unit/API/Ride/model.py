from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Rides(db.Model):
    __tableName__ = 'Rides'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    UserId = db.Column(db.Integer, db.ForeignKey('Users.id'))
    RideName = db.Column(db.String)
    RideCode = db.Column(db.String)
    AssembleDestination = db.Column(db.String(length=50), primary_key=True)

    def __init__(self, RideName, RideCode, AssembleDestination):
        self.RideName = RideName
        self.RideCode = RideCode
        self.AssembleDestination = AssembleDestination

    def __repr__(self):
        return f"{self.RideName}:{self.RideCode}:{self.AssembleDestination}"

    def json(self):
        return { "RideName": self.RideName, "RideCode": self.RideCode, "AssembleDestination": self.AssembleDestination}