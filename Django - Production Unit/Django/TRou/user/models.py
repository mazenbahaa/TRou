from django.db import models


class Users(models.Model):
    __tableName__ = 'Users'

    id = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

    def __init__(self, FirstName, LastName, Email, Location, Address, Password):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Location = Location
        self.Address = Address
        self.Password = Password

    def __repr__(self):
        return f"{self.FirstName}:{self.LastName}:{self.Email}:{self.Location}:{self.Address}:{self.Password}"

    
