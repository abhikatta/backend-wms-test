from django.urls import path
from .views import SignUpView, CurrentUserView
from constants import (
    SIGNUP_URL,
    USER_INFO_URL,
    LOGIN_URL,
    LOGOUT_URL,
    REFRESH_TOKEN_URL,
)

from accounts.views import LoginView, LogoutView, SignUpView, TokenRefreshView

urlpatterns = [
    path(SIGNUP_URL, SignUpView.as_view(), name="signup"),
    path(USER_INFO_URL, CurrentUserView.as_view(), name="user_info"),
    path(route=LOGIN_URL, view=LoginView.as_view(), name="login"),
    path(route=LOGOUT_URL, view=LogoutView.as_view(), name="logout"),
    path(
        route=REFRESH_TOKEN_URL, view=TokenRefreshView.as_view(), name="token_refresh"
    ),
]
