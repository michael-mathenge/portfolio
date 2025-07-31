import os
import sys

# Add your project directory to the sys.path
path = '/home/your_username/portfolio'  # Replace 'your_username' with your PythonAnywhere username
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()