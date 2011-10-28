from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^monitor/', include('monitor.urls')),
    (r'^dbe/', include('dbe.urls')),
    (r'^proj/', include('proj.urls')),
    (r'^graph/', include('graph.urls')),
)

urlpatterns += patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^accounts/signup/$', 'account.signup'),
)


# admin
if False:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns('',
        (r'^admin/',include(admin.site.urls)),
    )

# enable static server in debug mode
from settings import DEBUG, MEDIA_ROOT, STATIC_ROOT
if DEBUG:
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': STATIC_ROOT
        }),
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': MEDIA_ROOT
        }),
    )
