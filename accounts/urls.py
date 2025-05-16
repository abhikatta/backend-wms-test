from django.urls import path
from .views import SignUpView, CurrentUserView
from constants import SIGNUP_URL, USER_INFO_URL

urlpatterns = [
    path(SIGNUP_URL, SignUpView.as_view(), name="signup"),
    path(USER_INFO_URL, CurrentUserView.as_view(), name="user_info"),
]
