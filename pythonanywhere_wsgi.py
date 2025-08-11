import os
import sys

# Add your project directory to the sys.path
path = '/home/michaelmathenge/portfolio'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()