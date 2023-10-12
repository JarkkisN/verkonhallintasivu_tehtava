## Sisällysluettelo:

1. [Asennusohjeet](/#Asennusohjeet)
   1. [Perinteinen asennus](/#Perinteinen-asennus)
   2. [Docker Compose -asennus](/#Docker-Compose--asennus)

2. [Raportti](/#Raportti)
   1. [Johdanto](/#Johdanto)
   2. [Arkkitehtuurin kuvaus](/#Arkkitehtuurin-kuvaus)
   3. [Toiminnot ja ratkaisut](/#Toiminnot-ja-ratkaisut)
   4. [Yhteenveto](/#Yhteenveto)



# Asennusohjeet

## Vaatimukset
- Python (vähintään 3.6)
- pip
- virtualenv (suositeltavaa)
- Docker (jos käytät Docker Composea)
- Docker Compose (jos käytät Docker Composea)

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

7. **Avaa selain** ja mene osoitteeseen http://127.0.0.1:8080 nähdäksesi sovelluksen toiminnassa.

8. **(Valinnainen) Luo admin-käyttäjä**

   Tietokantaan luotu valmiiksi admin käyttäjä:
   ```bash
   nimi: root
   salasana: root
   ```

   Jos haluat käyttää omaa Django Admin - käyttäjää, luo admin-käyttäjä seuraavasti:
   ```bash
   python manage.py createsuperuser
   ```
   Tämän jälkeen voit kirjautua sisään admin-paneeliin osoitteessa http://127.0.0.1:8080/admin/.

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

3. **Avaa selain** ja mene osoitteeseen http://127.0.0.1/ nähdäksesi sovelluksen toiminnassa.

## Lisätietoja
Lisätietoja Django-projektin konfiguroinnista ja käytöstä löydät Djangon virallisesta dokumentaatiosta.

---

# Raportti
## Johdanto 

Tämä projekti keskittyy luomaan keskitetyn hallintasivuston laboratorion laitteille ja palveluille. Tavoitteena on tarjota helppokäyttöinen ja tehokas työkalu laitteiden ja palveluiden hallintaan sekä seurantaan. 

## Arkkitehtuurin kuvaus 

Järjestelmä koostuu kolmesta pääkomponentista jotka tarjoaa Django: tietokannasta, backendistä ja frontendistä.

Käytimme SQLite-tietokantaa, joka sisältää Device-taulun. Tämä taulu tallentaa laitteiden tiedot, 
- Tyypin
- IP-osoitteen
- Nimen
- Mallin
- Hallintapaneelin linkin

Backend on rakennettu Django-kehitysalustalla. Käytimme Django ORM:ää tietojen hallintaan ja Djangon sisäänrakennettuja lomakkeita laitteiden lisäämiseen ja muokkaamiseen. 

Frontend koostuu HTML-templaatteista, jotka on tyylitelty Bootstrapilla. Templaatit tarjoavat käyttöliittymän laitteiden ja palveluiden hallintaan. 

## Toiminnot ja ratkaisut 

Käyttäjäroolit: Järjestelmässä on kaksi pääkäyttäjäroolia: admin ja käyttäjä. Adminilla on oikeudet lisätä, muokata ja poistaa laitteita, kun taas käyttäjällä on oikeudet vain katsella laitteita. Käyttäjältä ei vaadita kirjautumista. Laitteita voi lisätä pääsivun kautta "lisää laite" kohdasta jos on kirjautunut admin käyttäjällä, mutta laitteet lisääminen onnistuu myös admin-paneelin kautta.

Sivulla on myös hakutoiminto. Käyttäjät voivat etsiä laitteita nimen, tai niiden tietojen perusteella. Hakutoiminto perustuu Djangon ORM:ään ja se palauttaa laitteet, jotka vastaavat hakuehtoja.

Projektiin lisättiin klikkauslaskuri. Järjestelmässä on toiminto, joka seuraa, kuinka monta kertaa laitteen hallintapaneelin linkkiä on klikattu. Tämä tieto tallennetaan tietokantaan jota voi seurata admin-paneelista. 

## Yhteenveto:

Tämä projekti on suunniteltu tarjoamaan keskitetty hallintasivusto laboratorion laitteille ja palveluille. Se on rakennettu Django-kehitysalustalla ja koostuu tietokannasta, backendistä ja frontendistä. Käytimme SQLite-tietokantaa laitteiden tietojen tallentamiseen ja frontend on tyylitelty Bootstrapilla.

Järjestelmässä on kaksi käyttäjäroolia: admin ja käyttäjä, joilla on erilaiset oikeudet. Lisäksi sivustolla on hakutoiminto laitteiden etsimiseen ja klikkauslaskuri, joka seuraa laitteen hallintapaneelin linkin käyttöä.
