#!/bin/bash

set -e

UWSGI_CONTAINER=$(docker ps -q -f name=uwsgi-nursery)

if [ ${#UWSGI_CONTAINER} -gt 0 ]; then
    docker exec -it $UWSGI_CONTAINER python server/manage.py makemigrations $1
    docker exec -it $UWSGI_CONTAINER python server/manage.py migrate
fi