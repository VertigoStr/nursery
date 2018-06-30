FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y \
      gettext \
      binutils \
      libproj-dev \
      gdal-bin && \
  apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /srv/project/src/ && mkdir -p /srv/project/media

WORKDIR /srv/project/src/

RUN pip install --upgrade pip && \
    pip install uwsgi && \
    rm -rf /root/.cache

COPY server/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache

RUN mkdir /srv/project/src/client/
COPY ./client/src/ /srv/project/src/client/src/

COPY . /srv/project/src/

ARG DJANGO_SETTINGS_MODULE=core.settings.dev
ENV DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
RUN python server/manage.py collectstatic --noinput
