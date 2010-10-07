# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from main.models import Contact


class CalendarWidget(forms.TextInput):
    """ Calendar widget """

    class Media:
        js = ('/jsi18n/',
              settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',)
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField',
                                                    'size': '10'})


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=_('Name'),
                           error_messages={'required':
                                           _("Enter your name, please")})
    surname = forms.CharField(max_length=50, label=_('Surname'),
                              error_messages={'required':
                                              _("Enter your surname, please")})
    birthday = forms.DateField(input_formats=["%d.%m.%Y", "%Y-%m-%d"],
                               label=_("Birthday"), required=False,
                               widget=CalendarWidget)
    bio = forms.CharField(widget=forms.Textarea(), label=_('Biography'),
                          required=False)
    email = forms.EmailField(max_length=50, widget=forms.TextInput(),
                             label=_("E-mail"), required=False)
    phone = forms.CharField(max_length=13, label=_('Phone'), required=False)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder.reverse()

    class Meta:
        model = Contact
