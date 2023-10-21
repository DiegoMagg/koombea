from os import environ, path

from koombea.default_settings import *

# Django

INSTALLED_APPS += [
    'accounts',
]

AUTH_USER_MODEL = 'accounts.User'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('POSTGRES_DB', 'postgres'),
        'USER': environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': environ.get('POSTGRES_HOST', 'localhost'),
        'POST': 5432,
    },
}

LOGIN_REDIRECT_URL = '/page-urls'

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
