FROM python:3.11.4

ENV DJANGO_SUPERUSER_USERNAME=user
ENV DJANGO_SUPERUSER_PASSWORD=password
ENV DJANGO_SUPERUSER_EMAIL=user@example.com


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

RUN python3 manage.py createsu --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL \
    --password $DJANGO_SUPERUSER_PASSWORD

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]