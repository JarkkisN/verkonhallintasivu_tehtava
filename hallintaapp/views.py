# Tuodaan tarvittavat moduulit ja funktiot Django-kirjastosta.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Device
from .forms import DeviceForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # Q-objekti mahdollistaa monimutkaisemmat tietokantahaut.

# Näkymä, joka näyttää listan laitteista.
def device_list(request):
    # Haetaan hakusana pyynnöstä.
    query = request.GET.get('q')
    # Jos hakusana on annettu, haetaan laitteet, jotka vastaavat hakusanaa.
    if query:
        devices = Device.objects.filter(
            Q(name__icontains=query) |
            Q(model__icontains=query) |
            Q(type__icontains=query) |
            Q(ip_address__icontains=query)
        )
    # Jos hakusanaa ei ole annettu, haetaan kaikki laitteet.
    else:
        devices = Device.objects.all()

    # Määritellään laitetyypit, joita voidaan käyttää templaateissa.
    device_types = ["ROUTER", "SWITCH", "NAS", "ePDU", "PROXMOX"]
    return render(request, 'device_list.html', {'devices': devices, 'device_types': device_types})

# Näkymä, joka mahdollistaa uuden laitteen lisäämisen.
# Tämä näkymä vaatii käyttäjän kirjautumisen.
@login_required
def add_device(request):
    # Jos pyyntö on POST-tyyppiä, käsitellään lomakkeen tiedot.
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        # Jos lomake on validi, tallennetaan laite ja ohjataan käyttäjä laitelistaan.
        if form.is_valid():
            form.save()
            return redirect('device_list')
    # Jos pyyntö ei ole POST-tyyppiä, näytetään tyhjä lomake.
    else:
        form = DeviceForm()
    return render(request, 'add_device.html', {'form': form})

# Näkymä, joka ohjaa käyttäjän laitteen hallintapaneeliin ja kasvattaa klikkauslaskuria.
def redirect_to_device(request, pk):
    # Haetaan laite tietokannasta tai palautetaan 404-virhe, jos laitetta ei löydy.
    device = get_object_or_404(Device, pk=pk)
    # Kasvatetaan laitteen klikkauslaskuria.
    device.click_count += 1
    device.save()
    # Ohjataan käyttäjä laitteen hallintapaneeliin.
    return redirect(device.admin_link)
