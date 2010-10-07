# -*- coding: utf-8 -*-
from django.contrib import admin

from reqlog.models import RequestLog, ObjectActionLog


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['date', 'path', 'method', 'remote_address']
    list_display_links = ['path']
    list_per_page = 100
    search_fields = ['path', 'remote_address']
    ordering = ['-date']
    date_hierarchy = 'date'


class ObjectActionLogAdmin(admin.ModelAdmin):
    list_display = ['date', 'model', 'object_pk', 'action']
    list_display_links = ['model']
    list_per_page = 100
    search_fields = ['models', 'object_pk', 'action']
    ordering = ['-date']
    list_filter = ['action']
    date_hierarchy = 'date'


admin.site.register(RequestLog, RequestLogAdmin)
admin.site.register(ObjectActionLog, ObjectActionLogAdmin)
