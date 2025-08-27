#!/bin/bash
set -e  # Exit on any error

echo "=== BUILD START ==="
echo "Current directory: $(pwd)"
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

echo "=== Installing dependencies ==="
pip install --upgrade pip
pip install -r requirements.txt

echo "=== Verifying Django ==="
python -c "import django; print('Django version:', django.get_version())"

echo "=== BUILD COMPLETE ==="
