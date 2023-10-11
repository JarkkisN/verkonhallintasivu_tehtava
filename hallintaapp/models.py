from django.db import models

class Device(models.Model):
    DEVICE_TYPES = (
        ('ROUTER', 'Reititin'),
        ('SWITCH', 'Kytkin'),
        ('NAS', 'NAS'),
        ('ePDU', 'ePDU'),
        ('PROXMOX', 'Proxmox'),
        # Lisää muita laitetyyppejä tarvittaessa
    )

    type = models.CharField(max_length=10, choices=DEVICE_TYPES)
    ip_address = models.GenericIPAddressField()
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    admin_link = models.URLField(blank=True, null=True)
    click_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
