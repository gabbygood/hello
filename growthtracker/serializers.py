# serializers.py
from rest_framework import serializers
from .models import PlantGrowthEvent

class PlantGrowthEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantGrowthEvent
        fields = ['id', 'user', 'date', 'description']
        read_only_fields = ['id', 'user']
