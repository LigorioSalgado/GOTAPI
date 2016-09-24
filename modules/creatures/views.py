from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Creature
from .serializers import CreatureSerializer


class ListCreatures(APIView):

	def get(self,request):

		creatures = Creature.objects.all()
		serializer = CreatureSerializer(creatures,many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = CreatureSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class DetailCreature(APIView):
	pass
# Create your views here.
