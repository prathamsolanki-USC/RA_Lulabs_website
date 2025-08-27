#!/usr/bin/env python3
import sys
import os

print("=== BUILD ENVIRONMENT TEST ===")
print(f"Python version: {sys.version}")
print(f"Current directory: {os.getcwd()}")
print(f"Files in directory: {os.listdir('.')}")

try:
    import django
    print(f"Django version: {django.get_version()}")
    print("Django import: SUCCESS")
except ImportError as e:
    print(f"Django import: FAILED - {e}")

try:
    import gunicorn
    print("Gunicorn import: SUCCESS")
except ImportError as e:
    print(f"Gunicorn import: FAILED - {e}")

print("=== TEST COMPLETE ===")
