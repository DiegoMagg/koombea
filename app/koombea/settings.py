from os import environ, path

import sentry_sdk
from koombea.default_settings import *
from sentry_sdk.integrations.django import DjangoIntegration

# Django

INSTALLED_APPS += [
    'accounts',
    'page',
]

AUTH_USER_MODEL = 'accounts.User'

ALLOWED_HOSTS = environ.get('ALLOWED_HOSTS', '').split(',')

CSRF_TRUSTED_ORIGINS = environ.get('CSRF_TRUSTED_ORIGINS', '').split(',')

SECRET_KEY = environ.get('SECRET_KEY', '').split(',')

DEBUG = int(environ.get('DJANGO_DEBUG', 0))

# Sentry

sentry_sdk.init(
    dsn=environ.get('SENTRY_DSN', ''),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

# Static files

MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

STORAGES = {
    'default': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    }
}

STATIC_URL = '/static/'

STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB', 'postgres'),
        'USER': environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
        'PORT': int(environ.get('POSTGRES_PORT', 5432)),
    },
}

LOGIN_REDIRECT_URL = '/page'

# Template

TEMPLATES += [
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'environment': 'koombea.jinja2.environment'
        },
    },
]

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
