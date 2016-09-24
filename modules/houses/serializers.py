from rest_framework import serializers
from modules.characters.serializers import CharacterSerializer
from .models import House

class HouseSerializer(serializers.ModelSerializer):
	members = serializers.StringRelatedField(many=True) #STRING SERIALIZER
	members = CharacterSerializer(many=True, read_only=True) # NESTED SERIALIZER 

	class Meta:
		model = House
		fields = ('name','words','coat_of_arms','house_image','members')