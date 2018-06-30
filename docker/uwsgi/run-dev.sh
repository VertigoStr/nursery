#!/bin/bash

pip install -r /srv/project/src/server/requirements.txt
source /srv/project/src/docker/uwsgi/collectstatic.sh &
python /srv/project/src/server/manage.py migrate --noinput

uwsgi /srv/project/src/docker/uwsgi/uwsgi-dev.ini
