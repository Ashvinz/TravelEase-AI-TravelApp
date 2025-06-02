# travelease_backend/vehicles/serializers.py
from rest_framework import serializers
from .models import Vehicle, VehicleType

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ['id', 'name', 'description']

class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type_name = serializers.CharField(source='vehicle_type.name', read_only=True)
    # image field is handled by DRF to provide URL path
    # vehicle_type (write) is the ID of the VehicleType
    vehicle_type = serializers.PrimaryKeyRelatedField(queryset=VehicleType.objects.all())


    class Meta:
        model = Vehicle
        fields = [
            'id', 'name', 'description', 'vehicle_type', 'vehicle_type_name',
            'license_plate', 'capacity', 'price_per_day', 'location',
            'status', 'image'
        ]
        extra_kwargs = {
            'image': {'required': False, 'allow_null': True}
        }