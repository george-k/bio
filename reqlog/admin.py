# -*- coding: utf-8 -*-
from django.contrib import admin
from reqlog.models import RequestLog


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['date', 'path', 'method', 'remote_address']
    list_display_links = ['path']
    list_per_page = 100
    search_fields = ['path', 'remote_address']
    ordering = ['-date']

admin.site.register(RequestLog, RequestLogAdmin)
