import os
import sys
import django.core.handlers.wsgi
from google.appengine.api import memcache

import settings
import django.conf

'''
= Load Django setting =
  Ref: http://stackoverflow.com/questions/5122414/django-googleappengine-error-django-settings-module-is-undefined

'''
# Filter out all the non-setting attributes of the settings module
settingsKeys = filter(lambda name: str(name) == str(name).upper(), dir(settings))
# copy all the setting values from the settings module into a dictionary
settingsDict = dict(map(lambda name: (name, getattr(settings, name)), settingsKeys))
django.conf.settings.configure(**settingsDict)
# os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

sys.modules['memcache'] = memcache
app = django.core.handlers.wsgi.WSGIHandler()
