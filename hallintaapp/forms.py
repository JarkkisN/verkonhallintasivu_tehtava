# forms.py
# Tuodaan tarvittavat moduulit ja funktiot Django-kirjastosta.
from django import forms
# Tuodaan Device-malli, jota käytetään lomakkeessa.
from .models import Device

# Luodaan DeviceForm-luokka, joka perii Django-lomakkeen ModelForm-luokan.
# Tämä lomake mahdollistaa laitteen tietojen lisäämisen ja muokkaamisen.
class DeviceForm(forms.ModelForm):
    # Meta-luokka määrittelee lomakkeen asetukset.
    class Meta:
        # Määritellään, että lomake käyttää Device-mallia.
        model = Device
        # Määritellään, mitkä kentät mallista sisällytetään lomakkeeseen.
        fields = ['type', 'ip_address', 'name', 'model', 'admin_link']
