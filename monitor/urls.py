from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',
    (r'^$', views.v_home),
    (r'^sysinfo$', views.v_sysinfo),

    (r'^services$', views.v_services),
    (r'^services/create$', views.v_services_create),
    (r'^services/ajax/show$', views.v_services_ajax_show),
    (r'^services/ajax/ctrl$', views.v_services_ajax_ctrl),

    (r'^processes$', views.v_processes),
    (r'^processes/create$', views.v_processes_create),
    (r'^processes/ajax/show$', views.v_processes_ajax_show),
    (r'^processes/ajax/ctrl$', views.v_processes_ajax_ctrl),

    (r'^cmd$', views.v_cmd),
    (r'^cmd/ajax/exec$', views.v_cmd_ajax_exec),
    (r'^cmd/ajax/create$', views.v_cmd_ajax_create),
)
