#!/bin/sh
set -eu
export PYTHONUNBUFFERED=1

echo "Starting Django startup sequence..."

# Skip migrations for now to isolate startup issues
# python3 manage.py migrate --noinput
# python3 manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec python3 -m gunicorn \
  --workers "${WEB_CONCURRENCY:-2}" \
  --bind "0.0.0.0:${PORT:-8000}" \
  --access-logfile - \
  --error-logfile - \
  --log-level debug \
  api_website.wsgi:application
