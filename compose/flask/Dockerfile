FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

COPY ./requirements /requirements
RUN pip install --upgrade pip
RUN pip install -r /requirements/base.txt

WORKDIR /app