from django.shortcuts import render
from .models import Character
from .serializer import Characterserializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CharacterDetail(APIView):
	def get_object(self, pk):
		try:
			return Character.objects.get(pk=pk)
		except Character.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		character = self.get_object(pk)
		serializer = CharacterSerializer(character)
		return Response(serializer.data)

	