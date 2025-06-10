from python:3.12.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ../.. /app

RUN pip install --no-cache-dir -r requirements.txt