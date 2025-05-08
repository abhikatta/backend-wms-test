# Create your views here.
from .models import Crew
from rest_framework import viewsets, permissions
from .serializers import CrewSerializer


class CrewViewSet(viewsets.ModelViewSet):
    serializer_class = CrewSerializer
    queryset = Crew.objects.all()
    permission_classes = [permissions.AllowAny]
