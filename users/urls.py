from django.urls import path, include
from django.conf import settings
from rest_framework import permissions
from .views import UserRegisterView, UserMeView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('me/', UserMeView.as_view(), name='user-me'),
]
