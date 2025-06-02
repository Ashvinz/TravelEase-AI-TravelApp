from django.contrib import admin
from .models import VehicleType, Vehicle
from django.utils.translation import gettext_lazy as _
from django.contrib.admin import SimpleListFilter
from django.db.models import Q


# Register your models here.
@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'license_plate', 'status', 'price_per_day')
    list_filter = ('status', 'vehicle_type')
    search_fields = ('name', 'license_plate', 'location')
    raw_id_fields = ('vehicle_type',) # Better for FKs with many options