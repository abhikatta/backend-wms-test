"""
URL configuration for main project.

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
import constants as constants
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from constants import LOGIN_URL, REFRESH_TOKEN_URL

# basically any url that starts from /url-name will be routed to the urls module of that app(feature)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(f"{constants.CREW}.urls")),
    path("", include(f"{constants.ROLES}.urls")),
    path("", include(f"{constants.ACCOUNTS}.urls")),
    # below is automatic for login, send username(email) and password for login in POST
    path(LOGIN_URL, TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(REFRESH_TOKEN_URL, TokenRefreshView.as_view(), name="token_refresh"),
] + debug_toolbar_urls()
