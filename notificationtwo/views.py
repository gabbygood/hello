from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class NotificationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # `user` is the target recipient
        # `request.user` is the sender (e.g., admin)
        serializer.save(sender=self.request.user)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def mark_all_notifications_read(request):
    Notification.objects.filter(user=request.user).update(is_read=True)
    return Response({'message': 'All notifications marked as read'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_notifications(request):
    Notification.objects.filter(user=request.user).delete()
    return Response({"detail": "All notifications deleted successfully."})

