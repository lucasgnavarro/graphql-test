# Dockerfile

FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY apps/ /app/
COPY config/ /app/
COPY demo_data/ /app/
COPY manage.py /app/
