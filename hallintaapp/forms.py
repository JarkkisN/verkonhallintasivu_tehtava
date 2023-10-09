# forms.py
from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['type', 'ip_address', 'name', 'model', 'admin_link']
