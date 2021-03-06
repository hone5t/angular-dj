import os
from .base import *

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY','')
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}