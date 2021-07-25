FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt