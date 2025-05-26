#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

# Verify static files were collected
echo "Verifying static files..."
ls -la staticfiles/

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

echo "Build completed successfully!"
