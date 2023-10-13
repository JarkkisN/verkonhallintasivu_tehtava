# apin urls.py

# Tuodaan tarvittavat moduulit Django-kirjastosta.
from django.urls import path
from . import views

# Määritellään URL-kuuntelijat ja niihin liittyvät näkymät.
urlpatterns = [
    # Juuripolku, joka ohjaa käyttäjän laitelistaan.
    path('', views.device_list, name='device_list'),
    
    # Polku, joka ohjaa käyttäjän laitteen lisäyslomakkeeseen.
    path('add/', views.add_device, name='add_device'),
    
    # Polku, joka ohjaa käyttäjän laitteen hallintapaneeliin.
    # Tämä polku ottaa vastaan laitteen yksilöivän avaimen (pk) osana URL-osoitetta.
    path('redirect-to-device/<int:pk>/', views.redirect_to_device, name='redirect_to_device'),
]
