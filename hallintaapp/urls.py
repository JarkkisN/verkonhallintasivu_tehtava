# apin urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('add/', views.add_device, name='add_device'),
    path('redirect-to-device/<int:pk>/', views.redirect_to_device, name='redirect_to_device'),
]
