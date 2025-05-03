from django.urls import path

from . import views


# this is basically url configuration
urlpatterns = [
    path('hello/', views.say_hello)
]
