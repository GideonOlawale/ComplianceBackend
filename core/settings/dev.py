'''Use this for development'''

from .base import *


ALLOWED_HOSTS += ['127.0.0.1:8000','localhost:3000','127.0.0.1:5000']
DEBUG = True

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sdx',
        'USER':'postgres',
        'PASSWORD':'swagger10net',
        'HOST':'localhost',
        'PORT': ''
    }
}
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5000",
)
CORS_ORIGIN_ALLOW_ALL = True
