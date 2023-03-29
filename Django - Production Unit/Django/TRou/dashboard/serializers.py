from rest_framework import serializers
from .models import Routes

class RideSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routes
		fields ='__all__'