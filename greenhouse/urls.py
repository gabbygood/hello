from django.urls import path
from .views import GreenhouseListCreateAPIView

urlpatterns = [
    path('greenhouses/', GreenhouseListCreateAPIView.as_view(), name='greenhouse-list-create'),
]
