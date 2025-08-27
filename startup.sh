#!/bin/bash
set -euo pipefail
export PYTHONUNBUFFERED=1

python3 manage.py migrate --noinput
python3 manage.py collectstatic --noinput

exec gunicorn \
  --workers "${WEB_CONCURRENCY:-2}" \
  --bind "0.0.0.0:${PORT:-8000}" \
  --access-logfile - \
  --error-logfile - \
  api_website.wsgi:application
