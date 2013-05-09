DEBUG = True
TEMPLATE_DEBUG = DEBUG


MIDDLEWARE_CLASSES = (
    'google.appengine.ext.ndb.django_middleware.NdbDjangoMiddleware',
    'django.middleware.common.CommonMiddleware',
)

INSTALLED_APPS = (
    'message',
    'libs',
)

ROOT_URLCONF = 'urls'

import os
ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

CACHE_BACKEND = 'memcached:///'
