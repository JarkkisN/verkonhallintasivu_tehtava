# Käytä virallista Python-kuvaa
FROM python:3.10-slim

# Aseta työhakemisto kontissa
WORKDIR /app

# Asenna Python-riippuvuudet
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Kopioi sovelluksen koodi konttiin
COPY . .

# Käynnistää Django-kehityspalvelimen määritetyssä osoitteessa ja portissa, kun Docker-kontti käynnistetään
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# Ilmoita Dockerille, että sovellus kuuntelee porttia 8000
EXPOSE 8000
