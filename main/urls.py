from django.contrib import admin
from django.urls import path, include
import constants as constants
from debug_toolbar.toolbar import debug_toolbar_urls


# basically any url that starts from /url-name will be routed to the urls module of that app(feature)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(f"{constants.CREW}.urls")),
    path("", include(f"{constants.ROLES}.urls")),
    path("", include(f"{constants.ACCOUNTS}.urls")),
    path("", include(f"{constants.CLIENTS}.urls")),
    # below is automatic for login, send username(email) and password for login in POST
] + debug_toolbar_urls()
