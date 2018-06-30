#!/bin/bash

set -e

UWSGI_CONTAINER=$(docker ps -q -f name=uwsgi-nursery)

if [ ${#UWSGI_CONTAINER} -gt 0 ]; then
    docker exec -it $UWSGI_CONTAINER python server/manage.py shell_plus
fi