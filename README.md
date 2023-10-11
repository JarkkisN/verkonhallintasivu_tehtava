# Django Projektin Käyttöönotto

Tämä on ohje Django-projektin ympäristön käyttöönottoon.

## Vaatimukset

- Python (vähintään 3.6)
- pip
- virtualenv (suositeltavaa)

## Asennusohjeet

1. **Kloonaa repositorio**

   ```bash
   git clone https://github.com/JarkkisN/verkonhallintasivu_tehtava
   cd repository
   ```

2. **Luo virtuaaliympäristö (suositeltavaa)**

   ```bash
   python -m venv venv
   ```

   Aktivoi virtuaaliympäristö:

   - Linux/macOS:

     ```bash
     source venv/bin/activate
     ```

   - Windows:

     ```bash
     .\venv\Scripts\activate
     ```

3. **Asenna riippuvuudet**

   ```bash
   pip install -r requirements.txt
   ```

4. **Määritä tietokanta**

   ```bash
   python manage.py migrate
   ```

5. **Käynnistä kehityspalvelin**

   ```bash
   python manage.py runserver
   ```

   Avaa selain ja mene osoitteeseen `http://127.0.0.1:8000/` nähdäksesi sovelluksen toiminnassa.

6. **(Valinnainen) Luo admin-käyttäjä**

   Jos haluat käyttää Django Admin -paneelia, luo admin-käyttäjä seuraavasti:

   ```bash
   python manage.py createsuperuser
   ```

   Tämän jälkeen voit kirjautua sisään admin-paneeliin osoitteessa `http://127.0.0.1:8000/admin/`.

## Lisätietoja

Lisätietoja Django-projektin konfiguroinnista ja käytöstä löydät [Djangon virallisesta dokumentaatiosta](https://docs.djangoproject.com/).

---
