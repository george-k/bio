# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('main.views',
    url(r'^$', 'show_contact'),
    url(r'^edit_contact/$', 'edit_contact'),
)
