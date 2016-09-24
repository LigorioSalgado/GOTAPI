from rest_framework import serializers
from .models import Character


class CharacterSerializer(serializers.ModelSerializer):

	class Meta: 
		model = Character
		fields = ('name','gender','birth_year','is_dead')

