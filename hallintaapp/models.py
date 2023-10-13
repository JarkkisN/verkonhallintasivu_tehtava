# Tuodaan Django-kirjaston models-moduuli, joka sisältää työkalut tietokantamallien luomiseen.
from django.db import models

# Luodaan Device-luokka, joka perii Django-kirjaston Model-luokan.
# Tämä luokka määrittelee laitteen tietokantamallin.
class Device(models.Model):
    # Määritellään vakiotuple, joka sisältää mahdolliset laitetyypit.
    # Jokainen tuple sisältää koodin ja sen selityksen.
    DEVICE_TYPES = (
        ('ROUTER', 'Reititin'),
        ('SWITCH', 'Kytkin'),
        ('NAS', 'NAS'),
        ('ePDU', 'ePDU'),
        ('PROXMOX', 'Proxmox'),
    )

    # Määritellään tietokantakentät ja niiden tyypit.
    type = models.CharField(max_length=10, choices=DEVICE_TYPES)  # Laitteen tyyppi
    ip_address = models.GenericIPAddressField()  # Laitteen IP-osoite
    name = models.CharField(max_length=255)  # Laitteen nimi
    model = models.CharField(max_length=255)  # Laitteen malli
    admin_link = models.URLField(blank=True, null=True)  # Linkki laitteen hallintapaneeliin (valinnainen)
    click_count = models.PositiveIntegerField(default=0)  # Laskuri, joka seuraa kuinka monta kertaa linkkiä on klikattu

    # Määritellään, miten laite esitetään merkkijonona (esim. admin-paneelissa).
    def __str__(self):
        return self.name
