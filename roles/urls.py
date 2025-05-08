from django.urls import include, path
from rest_framework.routers import DefaultRouter
from constants import ROLES_URL
from .views import RoleListView


router = DefaultRouter()

router.register("", RoleListView)

urlpatterns = [path(ROLES_URL, include(router.urls))]
