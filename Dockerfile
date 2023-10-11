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

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# Ilmoita Dockerille, että sovellus kuuntelee porttia 8000
EXPOSE 8000
