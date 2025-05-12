from django.urls import path
from .views import SignUpView
from constants import SIGNUP_URL

urlpatterns = [
    path(SIGNUP_URL, SignUpView.as_view(), name="signup"),
]
