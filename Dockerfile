FROM python:3.8.5

ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gunicorn3 gunicorn -y

RUN mkdir /code
WORKDIR /code
RUN pip3 install pip -U
ADD requirements.txt /code/
RUN pip3 install -r requirements.txt
ADD . /code/