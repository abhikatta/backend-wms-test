from django.urls import include, path
from rest_framework.routers import DefaultRouter
from constants import ACCOUNTS_URL
from .views import AccountViewSet


router = DefaultRouter()

router.register('', AccountViewSet)

urlpatterns = [
    path(ACCOUNTS_URL, include(router.urls))
]
