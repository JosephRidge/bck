from rest_framework import serializers
from . models import device


class device_serializer(serializers.ModelSerializer):
    class Meta:
        model = device
        fields = '__all__'
