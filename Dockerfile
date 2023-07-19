FROM python:3.8.15-alpine

RUN apk update && apk add python3-dev gcc libc-dev

ENV DJANGO_SUPERUSER_PASSWORD=nicepassword
ENV DJANGO_SUPERUSER_EMAIL=djangoadmin@agtools.com
ENV DJANGO_SUPERUSER_USERNAME=admin

WORKDIR /app

RUN pip install --upgrade pip
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./agtools /app/agtools

ADD ./server-entrypoint.sh /app/
RUN chmod +x ./server-entrypoint.sh
