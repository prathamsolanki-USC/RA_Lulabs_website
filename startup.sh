#!/bin/bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --workers 2 api_website.wsgi:application --bind 0.0.0.0:8000
