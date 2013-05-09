from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'message.views',
    (r'^write/$', 'write'),
    (r'^(\d+)$', 'index'),
    (r'^$', 'index'),
)
