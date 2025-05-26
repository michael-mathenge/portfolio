#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p staticfiles

# Set proper permissions
chmod -R 755 staticfiles

# Copy static files to staticfiles directory
echo "Copying static files..."
cp -r static/* staticfiles/ || true

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

echo "Build completed successfully!"
