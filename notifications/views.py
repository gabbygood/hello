from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_notification(request):
    title = request.data.get('title')
    message = request.data.get('message')

    if not title or not message:
        return Response({'error': 'Title and message are required.'}, status=status.HTTP_400_BAD_REQUEST)

    notification = Notification.objects.create(
        user=request.user,  # ✅ store the sender
        title=title,
        message=message,
    )

    return Response({
        'id': notification.id,
        'title': notification.title,
        'message': notification.message,
        'created_at': notification.created_at,
        'user_email': notification.user.email,
    }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_notifications(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    data = [
        {
            'id': notif.id,
            'title': notif.title,
            'message': notif.message,
            'created_at': notif.created_at.isoformat(),
        }
        for notif in notifications
    ]
    return Response(data)