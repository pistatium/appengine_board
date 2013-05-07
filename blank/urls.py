from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'blank.views',
    (r'^write/$', 'write'),
    (r'^.*$', 'index'),
)
