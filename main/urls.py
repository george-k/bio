# -*- coding: utf-8 -*-
from django.conf.urls.defaults import url, patterns
import main.views


urlpatterns = patterns('',
    url(r'^$', main.views.show_contact),
)
