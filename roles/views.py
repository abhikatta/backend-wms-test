from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

ROLES = [
    {"value": "carpenter", "label": "Carpenter"},
    {"value": "plumber", "label": "Plumber"},
    {"value": "electrician", "label": "Electrician"},
    {"value": "mason", "label": "Mason"},
]


class RoleListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        roles = ROLES
        return Response(roles)
