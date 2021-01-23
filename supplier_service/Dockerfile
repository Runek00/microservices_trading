FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt update && apt install gcc -y && apt clean

RUN pip3 install -r /app/requirements.txt

COPY . /app/