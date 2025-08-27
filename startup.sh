#!/bin/bash
python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --workers 2 api_website.wsgi
