from django.urls import path
from .views import PlantGrowthEventViewSet
from rest_framework.routers import SimpleRouter

event_list = PlantGrowthEventViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

event_detail = PlantGrowthEventViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

event_clear_all = PlantGrowthEventViewSet.as_view({
    'delete': 'clear_all',
})

urlpatterns = [
    path('api/events/', event_list, name='event-list'),
    path('api/events/<int:pk>/', event_detail, name='event-detail'),
    path('api/events/clear_all/', event_clear_all, name='event-clear-all')
]
