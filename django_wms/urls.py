"""
URL configuration for django_wms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .constants import APP_NAMES

urlpatterns = [
    path('admin/', admin.site.urls),
    # basically any url that starts from /playground will be routed to the urls module of that app(feature)
    path(f'{APP_NAMES.PLAYGROUND}/',
         include(f'{APP_NAMES.PLAYGROUND}.urls'))
]
