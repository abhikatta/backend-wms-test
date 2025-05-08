from django.urls import path
from .views import RoleListView
from constants import ROLES_URL

urlpatterns = [
    path(f"{ROLES_URL}", RoleListView.as_view(), name="role-list"),
]
