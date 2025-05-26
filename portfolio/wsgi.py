"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Create the WSGI application
application = get_wsgi_application()

# Wrap with WhiteNoise for static files
application = WhiteNoise(
    application,
    root=os.path.join(Path(__file__).resolve().parent.parent, 'staticfiles'),
    prefix='/static/'
)
