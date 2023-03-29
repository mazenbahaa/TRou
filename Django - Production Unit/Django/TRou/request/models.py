from django.db import models

class Requests(models.Model):
    __tableName__ = 'Requests'

    id = models.IntegerField(primary_key=True)
    R_Names = models.CharField(max_length=100)
    R_Codes = models.CharField(max_length=100)
    AssembleDestination_Current = models.CharField(max_length=100)
    AssembleDestination_Request = models.CharField(max_length=100)

    def __init__(self, R_Names, R_Codes, AssembleDestination_Current, AssembleDestination_Request):
        self.R_Names = R_Names
        self.R_Codes = R_Codes
        self.AssembleDestination_Current = AssembleDestination_Current
        self.AssembleDestination_Request = AssembleDestination_Request

    def __repr__(self):
        return f"{self.R_Names}:{self.R_Codes}:{self.AssembleDestination_Current}:{self.AssembleDestination_Request}"
