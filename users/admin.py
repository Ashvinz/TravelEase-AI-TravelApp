# D:\TravelEaseProjectFinal\users\admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdminConfig(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active']
    search_fields = ('email', 'username', 'first_name', 'last_name')
    list_filter = ('user_type', 'is_staff', 'is_active', 'is_superuser')
    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile Info', {'fields': ('phone_number', 'profile_picture', 'user_type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Info', {'fields': ('email', 'first_name', 'last_name', 'phone_number', 'profile_picture', 'user_type')}),
    )

admin.site.register(CustomUser, CustomUserAdminConfig)