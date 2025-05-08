from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

ROLES = [
    ("carpenter", "Carpenter"),
    ("plumber", "Plumber"),
    ("electrician", "Electrician"),
    ("mason", "Mason"),
]


class RoleListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        roles = ROLES
        return Response(roles)
