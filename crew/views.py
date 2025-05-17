# Create your views here.
from .models import Crew
from rest_framework import viewsets, permissions
from .serializers import CrewSerializer


class CrewViewSet(viewsets.ModelViewSet):
    serializer_class = CrewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Crew.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
