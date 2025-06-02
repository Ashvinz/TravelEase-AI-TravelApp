# travelease_backend/vehicles/views.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend # Correct import
from .models import Vehicle, VehicleType
from .serializers import VehicleSerializer, VehicleTypeSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all().order_by('name')
    serializer_class = VehicleTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read for anyone

    def get_permissions(self): # More granular for write operations
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all().select_related('vehicle_type').order_by('name')
    serializer_class = VehicleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read for anyone

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'vehicle_type__name': ['exact', 'icontains'], # Filter by name of related type
        'vehicle_type': ['exact'], # Filter by ID of related type
        'location': ['icontains'],
        'capacity': ['exact', 'gte', 'lte'],
        'status': ['exact'],
        'price_per_day': ['exact', 'gte', 'lte'],
    }
    search_fields = ['name', 'description', 'license_plate', 'location']
    ordering_fields = ['price_per_day', 'capacity', 'name', 'status']

    def get_permissions(self): # More granular for write operations
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()