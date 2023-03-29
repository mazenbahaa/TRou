from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Routes(db.Model):
    __tableName__ = "Routes"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    RouteName = db.Column(db.String(length=100), primary_key=True)
    RouteCode = db.Column(db.String, primary_key=True)
    StartPoint = db.Column(db.String(length=50))
    EndPoint = db.Column(db.String(length=50))
    DriverLicence = db.Column(db.Integer, unique=True)
    VehicleLicence = db.Column(db.Integer, unique=True, primary_key=True)
    AssemblePoint = db.Column(db.String(length=100))

    def __init__(self, RouteName, RouteCode, StartPoint, EndPoint, DriverLicence, VehicleLicence, AssemblePoint):
        self.RouteName = RouteName
        self.RouteCode = RouteCode
        self.StartPoint = StartPoint
        self.EndPoint = EndPoint
        self.DriverLicence = DriverLicence
        self.VehicleLicence = VehicleLicence
        self.AssemblePoint = AssemblePoint

    def __repr__(self):
        return f"{self.RouteName}:{self.RouteCode}:{self.StartPoint}:{self.EndPoint}:{self.DriverLicence}:{self.VehicleLicence}:{self.AssemblePoint}"

    def json(self):
        return {"RouteName": self.RouteName, "RouteCode": self.RouteCode, "StartPoint": self.StartPoint, "EndPoint": self.EndPoint, "DriverLicence": self.DriverLicence, "VehicleLicence": self.VehicleLicence, "AssemblePoint": self.AssemblePoint}