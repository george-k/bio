# -*- coding: utf-8 -*-
from django.contrib import admin

from main.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'surname', 'birthday']
    list_display_links = ['name']
    list_per_page = 50
    search_fields = ['name', 'surname']
    ordering = ['id']

admin.site.register(Contact, ContactAdmin)
