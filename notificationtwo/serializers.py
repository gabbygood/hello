from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender_email = serializers.EmailField(source='sender.email', read_only=True)  # optional

    class Meta:
        model = Notification
        fields = [
            'id', 'user', 'sender', 'sender_email', 'notif_type', 'title', 'message',
            'created_at', 'is_read'
        ]
        read_only_fields = ['created_at']
