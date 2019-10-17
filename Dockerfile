FROM python:3.5-alpine

COPY . /app

WORKDIR /app

RUN pip install nose2[coverage_plugin]>=0.6.5
