from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^$', views.home),
    (r'^dbviews$', views.v_dbviews),
    (r'^dbviews/(?P<nid>\w+)$', views.v_dbviews_show),

    (r'^explorer$', views.v_explorer),
    (r'^explorer/ajax/exec$', views.v_explorer_ajax_exec),
    (r'^explorer/ajax/create$', views.v_explorer_ajax_create),
)
