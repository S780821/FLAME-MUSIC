FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
RUN apt install ffmpeg -y

# Use official Node image as base (includes npm & cleans up layers better)
FROM node:20-slim

# Or if you want to keep your Debian base:
FROM python:3.11-slim-bookworm  (or whatever your current base is)
RUN apt-get update && apt-get install -y curl ca-certificates gnupg
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
RUN apt-get install -y nodejs

RUN mkdir /app/
COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -U -r requirements.txt

CMD python3 main.py
