from django.shortcuts import render

# Create your views here.
# lets get the data back by requesting the api for it.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import user
from . serializers import user_serializer


class user_list(APIView):
    def get(self, request):
        user_1 = user.objects.all()
        serializer = user_serializer(user_1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
