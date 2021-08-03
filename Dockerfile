FROM python:3
ENV PYTHONUNBUFFERED=1
RUN apt-get -y update
RUN apt-get -y upgrade
WORKDIR /code
COPY . /code/
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:8002 --access-logfile - ep_workspace_api.wsgi:application