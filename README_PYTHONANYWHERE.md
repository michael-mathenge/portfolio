# Deploying to PythonAnywhere

This guide explains how to deploy your Django application to PythonAnywhere.

## Prerequisites

1. A PythonAnywhere account (free tier available)
2. A MySQL database set up on PythonAnywhere

## Deployment Steps

### 1. Upload Your Code

You can upload your code using Git or SFTP:

```bash
# Using Git (recommended)
git clone https://github.com/your_username/portfolio.git
```

### 2. Set Up Virtual Environment

In a PythonAnywhere console:

```bash
mkvirtualenv portfolio-env --python=/usr/bin/python3.8
pip install -r requirements.txt
```

### 3. Configure Environment Variables

In the PythonAnywhere web interface:
1. Go to the "Web" tab
2. Select your web app
3. In the "Environment variables" section, add:
   - `SECRET_KEY`: your_secret_key_here
   - `DEBUG`: False
   - `PYTHONANYWHERE_USERNAME`: your_pythonanywhere_username
   - `PYTHONANYWHERE_DATABASE_URL`: mysql://username:password@hostname/database_name

### 4. Configure Database

1. Create a MySQL database in PythonAnywhere:
   - Go to the "Databases" tab
   - Create a new MySQL database
   - Note the hostname, username, and password

2. Update your database settings in the environment variables:
   - `PYTHONANYWHERE_DATABASE_URL`: mysql://your_username:your_password@your_username.mysql.pythonanywhere-services.com/your_username$portfolio

### 5. Run Migrations

In a PythonAnywhere console:

```bash
cd /home/your_username/portfolio
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 6. Configure Web App

In the PythonAnywhere web interface:

1. Go to the "Web" tab
2. Create a new web app or edit existing one
3. Set the following:
   - Source code: `/home/your_username/portfolio`
   - Working directory: `/home/your_username/portfolio`
   - Virtual environment path: `/home/your_username/.virtualenvs/portfolio-env`
   - WSGI file: `/home/your_username/portfolio/pythonanywhere_wsgi.py`

4. Configure static files:
   - URL: `/static/`
   - Path: `/home/your_username/portfolio/staticfiles`

### 7. Reload the Web App

After configuration, click the "Reload" button to apply changes.

## Shell Access

PythonAnywhere provides excellent shell access:

1. Go to the "Consoles" tab in your dashboard
2. Start a new Bash console
3. Navigate to your project directory
4. Run any Django management commands:

```bash
cd /home/your_username/portfolio
python manage.py changepassword Mathenge
```

## Troubleshooting

### Common Issues

1. **Database Connection Errors**:
   - Check your database URL format
   - Ensure the database exists and is accessible
   - Verify username and password

2. **Static Files Not Loading**:
   - Run `python manage.py collectstatic`
   - Check static files mapping in web configuration

3. **Module Not Found Errors**:
   - Ensure virtual environment is activated
   - Check that all requirements are installed

### Useful Commands

```bash
# Activate virtual environment
workon portfolio-env

# Install requirements
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Change admin password
python manage.py changepassword Mathenge

# Check database status
python manage.py showmigrations
```

## Environment Variables

Set these environment variables in the PythonAnywhere web interface:

- `SECRET_KEY`: Your Django secret key (generate a new one for production)
- `DEBUG`: Set to `False` for production
- `PYTHONANYWHERE_USERNAME`: Your PythonAnywhere username
- `PYTHONANYWHERE_DATABASE_URL`: Your MySQL database URL
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

## Differences from Render.com

1. **Database**: Uses MySQL instead of PostgreSQL
2. **Static Files**: Served directly by Apache
3. **Environment Variables**: Set through web interface
4. **Deployment**: Manual setup through web interface
5. **Shell Access**: Direct SSH-like console access

This setup allows you to run the same Django application on PythonAnywhere with the same functionality as on Render.com.