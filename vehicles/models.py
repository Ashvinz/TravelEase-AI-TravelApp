# travelease_backend/vehicles/models.py
from django.db import models
from django.conf import settings

class VehicleType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    AVAILABILITY_STATUS_CHOICES = (
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance', 'Maintenance'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True, related_name="vehicles")
    license_plate = models.CharField(max_length=20, unique=True)
    capacity = models.PositiveIntegerField(default=4)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=AVAILABILITY_STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to='vehicle_images/', blank=True, null=True)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='owned_vehicles')

    def __str__(self):
        return f"{self.name} ({self.license_plate})"