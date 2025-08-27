#!/bin/bash
set -e  # Exit on any error

echo "=== DJANGO STARTUP START ==="

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn server..."
gunicorn api_website.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 120

echo "=== DJANGO STARTUP COMPLETE ==="
