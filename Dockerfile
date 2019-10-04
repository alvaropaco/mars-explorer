FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

COPY . /app

WORKDIR /app

RUN pip install nose2[coverage_plugin]>=0.6.5