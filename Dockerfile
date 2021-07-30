FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get -y update
RUN apt-get -y upgrade
WORKDIR /code
COPY . /code/
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt