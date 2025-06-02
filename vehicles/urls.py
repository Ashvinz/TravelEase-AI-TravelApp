from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .views import VehicleViewSet, VehicleTypeViewSet

router = DefaultRouter()
router.register(r'types', VehicleTypeViewSet, basename='vehicletype')
router.register(r'', VehicleViewSet, basename='vehicle') # Root for /api/vehicles/

urlpatterns = [
    path('', include(router.urls)),
]
