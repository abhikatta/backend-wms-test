from django.urls import include, path
from rest_framework.routers import DefaultRouter
from constants import ACCOUNTS_URL
from .views import CrewViewSet


router = DefaultRouter()

router.register("", CrewViewSet)

urlpatterns = [path(ACCOUNTS_URL, include(router.urls))]
