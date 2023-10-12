# Django verkonhallintasivu tehtävän käyttöönotto ohjeet:
Tämä on ohje Django-projektin ympäristön käyttöönottoon.

## Vaatimukset
- Python (vähintään 3.6)
- pip
- virtualenv (suositeltavaa)
- Docker (jos käytät Docker Composea)
- Docker Compose (jos käytät Docker Composea)

## Asennusohjeet

### Perinteinen asennus

1. **Kloonaa repositorio**
   ```bash
   git clone https://github.com/JarkkisN/verkonhallintasivu_tehtava
   cd repository
   ```

2. **Luo virtuaaliympäristö (suositeltavaa)**
   ```bash
   python -m venv venv
   ```

3. **Aktivoi virtuaaliympäristö**:

   Linux/macOS:
   ```bash
   source venv/bin/activate
   ```
   Windows:
   ```bash
   .\venv\Scripts\activate
   ```

4. **Asenna riippuvuudet**
   ```bash
   pip install -r requirements.txt
   ```

5. **Määritä tietokanta**
   ```bash
   python manage.py migrate
   ```

6. **Käynnistä kehityspalvelin**
   ```bash
   python manage.py runserver
   ```

7. **Avaa selain** ja mene osoitteeseen http://127.0.0.1:8000/ nähdäksesi sovelluksen toiminnassa.

8. **(Valinnainen) Luo admin-käyttäjä**

   Jos haluat käyttää Django Admin -paneelia, luo admin-käyttäjä seuraavasti:
   ```bash
   python manage.py createsuperuser
   ```
   Tämän jälkeen voit kirjautua sisään admin-paneeliin osoitteessa http://127.0.0.1:8000/admin/.

### Docker Compose -asennus

1. **Kloonaa repositorio**
   ```bash
   git clone https://github.com/JarkkisN/verkonhallintasivu_tehtava
   cd repository
   ```

2. **Rakenna ja käynnistä kontit Docker Composella**
   ```bash
   docker-compose up --build
   ```

3. **Avaa selain** ja mene osoitteeseen http://127.0.0.1:8000/ nähdäksesi sovelluksen toiminnassa.

## Lisätietoja
Lisätietoja Django-projektin konfiguroinnista ja käytöstä löydät Djangon virallisesta dokumentaatiosta.

---
