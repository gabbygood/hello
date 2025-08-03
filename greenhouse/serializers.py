from rest_framework import serializers
from .models import Greenhouse

class GreenhouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Greenhouse
        fields = ['id', 'name', 'image', 'created_at']