from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from constants import ITEMS_URL

router = DefaultRouter()

router.register('', ItemViewSet)


urlpatterns = [
    path(ITEMS_URL, include(router.urls))
]
