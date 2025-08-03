from django.urls import path
from .views import send_notification, get_user_notifications

urlpatterns = [
    path('send/', send_notification, name='send_notification'),
    path('user/', get_user_notifications, name='get_user_notifications'),
]
