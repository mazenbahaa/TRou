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