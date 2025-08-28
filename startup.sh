#!/bin/bash

# Startup script for App Runner
echo "Starting Django application with Python 3.11..."

# Ensure proper Python environment
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Run database migrations if needed
echo "Running database migrations..."
python manage.py migrate --noinput

# Start the application
echo "Starting Gunicorn server..."
exec gunicorn api_website.wsgi:application \
    --bind 0.0.0.0:8000 \
    --timeout 120 \
    --workers 2 \
    --access-logfile - \
    --error-logfile - \
    --log-level info
