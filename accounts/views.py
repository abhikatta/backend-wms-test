
# Create your views here.
from .models import Account
from rest_framework import viewsets, permissions
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
