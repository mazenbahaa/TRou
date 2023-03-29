from dataclasses import fields
from django.forms import ModelForm
from .models import *


class ADriverForm(ModelForm):
    class Meta:
        model = users
        fields ='__all__'

class AReportForm(ModelForm):
    class Meta:
        model = Reports
        fields ='__all__'

class ARequestForm(ModelForm):
    class Meta:
        model = Requests
        fields ='__all__'

class AVehicleForm(ModelForm):
    class Meta:
        model = Vehicles
        fields ='__all__'

class ARideForm(ModelForm):
    class Meta:
        model = Routes
        fields ='__all__'