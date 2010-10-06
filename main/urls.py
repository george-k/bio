# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('main.views',
    url(r'^$', 'show_contact'),
    url(r'^edit_contact/$', 'edit_contact'),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login',
        {'template_name': 'login.html'}),
    url(r'^logout/$', 'logout', {'next_page': '/'},
        name="auth_logout"),
)
