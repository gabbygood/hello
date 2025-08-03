from django.urls import path
from .views import NotificationListCreateAPIView, delete_all_notifications, mark_all_notifications_read

urlpatterns = [
    path('notifications/user/', NotificationListCreateAPIView.as_view(), name='user-notifications'),
    path('notifications/mark_all_read/', mark_all_notifications_read, name='mark-all-read'),
    path('notifications/delete_all/', delete_all_notifications, name='delete-all-notifications'),
]
