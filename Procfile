web: gunicorn portfolio.wsgi:application --log-file -
worker: celery -A portfolio worker -l info
