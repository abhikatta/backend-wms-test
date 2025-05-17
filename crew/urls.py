from django.urls import include, path
from rest_framework.routers import DefaultRouter
from constants import CREW_URL
from .views import CrewViewSet


router = DefaultRouter()

router.register("", CrewViewSet, basename="crew")

urlpatterns = [path(CREW_URL, include(router.urls))]
