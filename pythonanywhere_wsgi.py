# WSGI configuration file for PythonAnywhere
# Copy the contents of this file to /var/www/<your-username>_pythonanywhere_com_wsgi.py on PythonAnywhere

import os
import sys

# Path to your project directory on PythonAnywhere
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'sid.settings'

# Initialize WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
