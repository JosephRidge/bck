from rest_framework import serializers
from . models import payload


class payload_serializer(serializers.ModelSerializer):
    class Meta:
        model = payload
        fields = '__all__'
