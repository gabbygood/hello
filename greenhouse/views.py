from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Greenhouse
from .serializers import GreenhouseSerializer

class GreenhouseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Greenhouse.objects.all().order_by('-created_at')
    serializer_class = GreenhouseSerializer
    parser_classes = [MultiPartParser, FormParser] 
