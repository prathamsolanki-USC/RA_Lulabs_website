#!/bin/bash
echo "Starting Django application..."
python manage.py collectstatic --noinput
python manage.py migrate --noinput
exec gunicorn api_website.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 120
