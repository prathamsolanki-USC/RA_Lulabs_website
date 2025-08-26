#!/bin/bash
set -e

echo "Starting Django build process..."

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run database migrations (if needed)
python manage.py migrate --noinput

echo "Build completed successfully!"
