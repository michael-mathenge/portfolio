#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create staticfiles directory and set permissions
rm -rf staticfiles
mkdir -p staticfiles
chmod -R 755 staticfiles

# Copy all static files to staticfiles directory
echo "Copying static files..."
cp -r static/. staticfiles/ || true

# Verify files were copied
echo "Contents of staticfiles directory:"
ls -la staticfiles/

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

# Verify collected files
echo "Contents of collected static files:"
find staticfiles -type f | sort

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

echo "Build completed successfully!"
