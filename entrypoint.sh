#!/bin/sh

args=$@

if [ -z "$args" ]; then
    python manage.py migrate
    python manage.py runserver 0.0.0.0:9000
else
    exec "$@"
fi
