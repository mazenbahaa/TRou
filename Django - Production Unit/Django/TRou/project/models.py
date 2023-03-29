from django.db import models


class users(models.Model):
    __tableName__ = 'users'
   
    DriverName = models.CharField(max_length=200, null=True)
    id = models.IntegerField(primary_key=True)
    Email = models.EmailField(max_length=250, null= True, unique= True)
    LicenseNumber = models.IntegerField()
    LicenseEnd = models.IntegerField()
    Ride = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __str__(self):
        return self.DriverName
    

class Routes(models.Model):
    __tableName__ = 'Routes'

    id = models.IntegerField(primary_key=True)
    RouteName = models.CharField(max_length=100)
    RouteCode = models.CharField(max_length=100)
    StartPoint = models.CharField(max_length=100)
    EndPoint = models.CharField(max_length=100)
    VehicleLicence = models.IntegerField()

    def __str__(self):
        return self.RouteName
    

class Rides(models.Model):
    __tableName__ = 'Rides'

    RideName = models.CharField(max_length=100)
    RideCode = models.CharField(max_length=100)
    AssembleDestination = models.CharField(max_length=100)

    def __str__(self):
          return self.RideName
   

class Vehicles(models.Model):
    __tableName__ = 'Vehicles'

    VehicleModel = models.CharField(max_length=100)
    VehicleCapacity = models.IntegerField()
    LicenceNumber = models.CharField(max_length=100)
    EndLicence = models.CharField(max_length=100)

    def __str__(self):
        return self.VehicleModel
    

class AssemblePoints(models.Model):
    __tableName__ = 'AssemblePoints'

    id = models.IntegerField(primary_key=True)
    R_Name = models.CharField(max_length=100)
    R_Code = models.CharField(max_length=100)
    R_Location = models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    AssemblePoints = models.CharField(max_length=100)

    def __str__(self):
        return self.R_Name
    

class Requests(models.Model):
    __tableName__ = 'Requests'

    R_Names = models.CharField(max_length=100)
    R_Codes = models.CharField(max_length=100)
    Ride_Current = models.CharField(max_length=100)
    Ride_Request = models.CharField(max_length=100, default='Helwan')
    Reasons = models.CharField(max_length=100)
    def __str__(self):
        return self.R_Names
    

class Reports(models.Model):
    __tableName__ = 'Reports'

    Name = models.CharField(max_length=100, default='Mark')
    Message = models.CharField(max_length=200)

    def __str__(self):
        return self.Name
  
 
