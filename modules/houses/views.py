from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import House
from .serializers import HouseSerializer
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .permissions import ApiUserPermissions
# Create your views here.


class ListHouses (APIView):
	permission_classes = (ApiUserPermissions,)
	authentication_classes = (JSONWebTokenAuthentication,)

	def get(self,request):

		

		houses = House.objects.all()
		serializer = HouseSerializer(houses,many=True)
		print (request.user.username)
		return Response(serializer.data)




class HouseDetail(APIView):

	permission_classes = (IsAuthenticated,)
	authentication_classes = (JSONWebTokenAuthentication,)


	def get_object(self, pk):
		try:
			return House.objects.get(pk=pk)
		except House.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		house = self.get_object(pk)
		serializer = HouseSerializer(house)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		house = self.get_object(pk)
		serializer = HouseSerializer(house, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		house = self.get_object(pk)
		house.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


