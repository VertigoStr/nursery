from django.conf import settings

from core.settings.base import *

DEBUG = True

ALLOWED_HOSTS = [
    'nursery.lvh.me',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nursery',
        'USER': 'nursery',
        'PASSWORD': 'nursery',
        'HOST': 'db-nursery',
        'PORT': '5432',
    },
}

if settings.DEBUG and os.getenv('ENABLE_DEBUG_TOOLBAR'):
    MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')
    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TOOLBAR_CALLBACK": lambda request: True,
    }
