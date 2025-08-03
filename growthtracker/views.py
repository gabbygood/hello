from rest_framework import viewsets, permissions
from .models import PlantGrowthEvent
from .serializers import PlantGrowthEventSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class PlantGrowthEventViewSet(viewsets.ModelViewSet):
    serializer_class = PlantGrowthEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PlantGrowthEvent.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['delete'], url_path='clear_all')
    def clear_all(self, request):
        try:
            events = self.get_queryset()
            deleted_count = events.count()
            events.delete()
            return Response({"detail": f"{deleted_count} events deleted."})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
