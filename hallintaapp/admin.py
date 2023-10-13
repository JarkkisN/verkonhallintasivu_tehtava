# Tuodaan tarvittavat moduulit Django-kirjastosta.
from django.contrib import admin
from .models import Device

# Rekisteröidään Device-malli Django-admin-paneeliin.
# Tämä mahdollistaa laitteiden hallinnan admin-paneelissa.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    # Määritellään, mitkä kentät näytetään laitelistanäkymässä admin-paneelissa.
    list_display = ('name', 'type', 'ip_address', 'model', 'admin_link')
    
    # Määritellään, mitkä kentät ovat haettavissa admin-paneelin hakutoiminnolla.
    search_fields = ('name', 'type', 'ip_address', 'model')
    
    # Määritellään suodattimet, joiden avulla voidaan suodattaa laitteita tietyillä kriteereillä.
    list_filter = ('type',)
