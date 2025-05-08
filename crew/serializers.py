from rest_framework import serializers
from .models import Crew


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
