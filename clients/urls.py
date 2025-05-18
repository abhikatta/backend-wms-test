from django.urls import include, path
from rest_framework.routers import DefaultRouter
from constants import CLIENTS_URL
from .views import ClientsViewSet


router = DefaultRouter()

router.register("", ClientsViewSet, basename="clients")

urlpatterns = [path(CLIENTS_URL, include(router.urls))]
