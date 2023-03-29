from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Vehicles(db.Model):
    __tableName__ = 'Vehicles'

    id = db.Column(db.Integer, primary_key=True)
    VehicleModel = db.Column(db.String(length=20))
    VehicleCapacity = db.Column(db.Integer)
    Licence = db.Column(db.String(length=8), db.ForeignKey('Routes.VehicleLicence'))
    EndLicence = db.Column(db.String(length=10))

    def __init__(self, VehicleModel, VehicleCapacity, Licence, EndLicence):
        self.VehicleModel = VehicleModel
        self.VehicleCapacity = VehicleCapacity
        self.Licence = Licence
        self.EndLicence = EndLicence
    
    def __repr__(self):
        return f"{self.VehicleModel}:{self.VehicleCapacity}:{self.Licence}:{self.EndLicence}"

    def json(self):
        return {"VehicleModel": self.VehicleModel, "VehicleCapacity": self.VehicleCapacity, "Licence": self.Licence, "EndLicence": self.EndLicence}