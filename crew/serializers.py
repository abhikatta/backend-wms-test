from rest_framework import serializers
from .models import Crew


class CrewSerializer(serializers.ModelSerializer):

    # first called and removes the pop fields from the response
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove user and client from fields to exclude them from serialized output
        self.fields.pop("user", None)
        self.fields.pop("client", None)

    # DRF automatically calls get_<name>(here name=client_name) and attaches the returned value
    # in the response as a :read only field:
    # as client_name: name_value if client exists
    client_name = serializers.SerializerMethodField()
    client_phone_number = serializers.SerializerMethodField()

    class Meta:
        model = Crew
        fields = "__all__"
        read_only_fields = ["id", "created_at"]

    def get_client_name(self, obj):
        if obj.client:
            return f"{obj.client.first_name} {obj.client.last_name}"
        return None

    def get_client_phone_number(self, obj):
        if obj.client:
            return obj.client.phone_number
        return None
