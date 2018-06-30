#!/bin/bash

# Default value
: ${DISABLE_COLLECTSTATIC:=0}

if [ $DISABLE_COLLECTSTATIC -eq 0 ]; then
    while [ 1 ]
    do
        python server/manage.py collectstatic --noinput &> /dev/null
        sleep 5
    done
else
    python server/manage.py collectstatic --noinput
fi
