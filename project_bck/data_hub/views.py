from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import payload
from . serializers import payload_serializer


class payload_list(APIView):
    def get(self, request):
        payload_1 = payload.objects.all()
        serializer = payload_serializer(payload_1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
