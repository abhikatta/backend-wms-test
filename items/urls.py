from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
import constants

router = DefaultRouter()

router.register(rf'{constants.ITEMS}', ItemViewSet)


urlpatterns = [
    path(f'{constants.API}', include(router.urls))
]
