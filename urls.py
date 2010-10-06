# -*- coding: utf-8 -*-
import sys
from django.conf.urls.defaults import url, patterns, include
import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

if 'runserver' in sys.argv:
    urlpatterns = patterns('',
        url(r'^media/(.*)$', 'django.views.static.serve', 
            kwargs={'document_root': settings.MEDIA_ROOT}),
    )
else:
    urlpatterns = []

urlpatterns += patterns('',
    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # Enable apps
    url(r'^', include('main.urls')),
)

