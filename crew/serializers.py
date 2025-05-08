from rest_framework import serializers
from .models import Crew


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "created_at",
            "role",
            "is_active",
            "is_tasked",
            "hourly_wage",
        ]
        read_only_fields = ["id", "created_at"]
