# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns
from django.views.generic import list_detail

from reqlog.models import RequestLog


last_10_requests = {'queryset': RequestLog.objects.order_by('-date')[0:10],
                    'template_name': 'last_10_requests.html'}

urlpatterns = patterns('main.views',
    url(r'^$', 'show_contact'),
    url(r'^edit_contact/$', 'edit_contact'),
    url(r'^request_logs_list/$', list_detail.object_list, last_10_requests,
        name="last_logs"),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'logout', {'next_page': '/'},
        name="auth_logout"),
)

#For calendar widget
urlpatterns += patterns('',
    (r'^jsi18n/', 'django.views.i18n.javascript_catalog'),
)
