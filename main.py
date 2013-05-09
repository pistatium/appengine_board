import os
import sys
import django.core.handlers.wsgi
from google.appengine.api import memcache

import settings
import django.conf

'''
= Load Django setting =
  cf. http://stackoverflow.com/questions/5122414/django-googleappengine-error-django-settings-module-is-undefined
'''
settingsKeys = filter(lambda name: str(name) == str(name).upper(), dir(settings))
settingsDict = dict(map(lambda name: (name, getattr(settings, name)), settingsKeys))
django.conf.settings.configure(**settingsDict)

sys.modules['memcache'] = memcache
app = django.core.handlers.wsgi.WSGIHandler()
