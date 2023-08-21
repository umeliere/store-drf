FROM python:3.10

WORKDIR /usr/src/store_drf

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /usr/src/store_drf
