# syntax=docker/dockerfile:1
FROM --platform=linux/amd64 python:3.8-slim-buster as build

# FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python", "./app.py"]