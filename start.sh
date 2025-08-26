#!/bin/bash
echo "Starting Django..."
python manage.py collectstatic --noinput
exec gunicorn api_website.wsgi:application --bind 0.0.0.0:8000 --workers 1
