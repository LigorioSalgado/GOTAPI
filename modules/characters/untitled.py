from rest_framework import serializers
from .models import House

class HouseSerializer(serializers.ModelSerializer):
	members = serializers.StringRelatedField(many=True)

	class Meta:
		model = House
		fields = ('name','words','coat_of_arms','house_image','members')