#!/usr/bin/env bash
# exit on error
set -o errexit
set -o pipefail

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

echo "Build completed successfully!"
