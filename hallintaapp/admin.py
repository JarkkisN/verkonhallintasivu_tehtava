from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'ip_address', 'model', 'admin_link')
    search_fields = ('name', 'type', 'ip_address', 'model')
    list_filter = ('type',)
