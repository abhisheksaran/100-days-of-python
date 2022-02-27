FROM python:3.9-alpine

RUN pip3 install --upgrade pip
COPY ./ /src
WORKDIR /src

RUN apk add tk
CMD python3 main.py
