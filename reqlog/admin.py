# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from reqlog.models import RequestLog, ObjectActionLog


class RequestLogAdmin(admin.ModelAdmin):
    list_display = ['date', 'path', 'method', 'remote_address', 'priority']
    list_display_links = ['path']
    list_per_page = 100
    search_fields = ['path', 'remote_address']
    ordering = ['-date']
    date_hierarchy = 'date'
    list_editable = ['priority']
    list_filter = ['priority']
    actions = ['set_to_default']

    def set_to_default(self, request, queryset):
        """ Set marked request logs priority to '0' """
        try:
            queryset.update(priority=0)
            self.message_user(request,
                              _('{n} entries was updated').\
                              format(n=len(queryset)))
        except Exception as error:
            self.message_user(request,
                              _('Logs rset to default failed'))
    set_to_default.short_description = _("Set priority to default value")


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
