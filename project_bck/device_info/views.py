from django.shortcuts import render

# Create your views here.
# lets get the data back by requesting the api for it.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import device
from . serializers import device_serializer


class device_list(APIView):
    def get(self, request):
        device_1 = device.objects.all()
        serializer = device_serializer(device_1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
