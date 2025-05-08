from rest_framework import serializers
from .models import Crew


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ["id", "first_name", "last_name", "email", "created_at"]
        read_only_fields = ["id", "created_at"]
