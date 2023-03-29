from django.db import models


class Vehicles(models.Model):
    __tableName__ = 'Vehicles'

    id = models.IntegerField(primary_key=True)
    VehicleModel = models.CharField(max_length=100)
    VehicleCapacity = models.IntegerField()
    Licence = models.CharField(max_length=100)
    EndLicence = models.CharField(max_length=100)

    def __init__(self, VehicleModel, VehicleCapacity, Licence, EndLicence):
        self.VehicleModel = VehicleModel
        self.VehicleCapacity = VehicleCapacity
        self.Licence = Licence
        self.EndLicence = EndLicence
    
    def __repr__(self):
        return f"{self.VehicleModel}:{self.VehicleCapacity}:{self.Licence}:{self.EndLicence}"
