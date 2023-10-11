from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Lisätty Q-objektin tuonti

def device_list(request):
    query = request.GET.get('q')
    if query:
        devices = Device.objects.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(type__icontains=query) |
            Q(ip_address__icontains=query)
        )
    else:
        devices = Device.objects.all()

    device_types = ["ROUTER", "SWITCH", "NAS", "ePDU", "PROXMOX"]
    return render(request, 'device_list.html', {'devices': devices, 'device_types': device_types})

@login_required
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})

def redirect_to_device(request, pk):
    device = get_object_or_404(Device, pk=pk)
    device.click_count += 1
    device.save()
    return redirect(device.admin_link)
