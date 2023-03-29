from django.db import models

class Ride(models.Model):
    __tableName__ = 'Rides'

    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    RideName = models.CharField(max_length=100)
    RideCode = models.CharField(max_length=100)
    AssembleDestination = models.CharField(max_length=100)

    def __init__(self, RideName, RideCode, AssembleDestination):
        self.RideName = RideName
        self.RideCode = RideCode
        self.AssembleDestination = AssembleDestination

    def __repr__(self):
        return f"{self.RideName}:{self.RideCode}:{self.AssembleDestination}"