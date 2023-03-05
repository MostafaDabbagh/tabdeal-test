# syntax=docker/dockerfile:1
FROM python:3.10.8
WORKDIR /project/src
COPY requirements.txt /project/
RUN pip install -r ../requirements.txt
COPY . /project/src/
