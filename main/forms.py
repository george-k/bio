# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, label=_('Name'),
                           error_messages={'required': \
                                           _("Enter your name, please")})
    surname = forms.CharField(max_length=50, label=_('Surname'),
                              error_messages={'required': \
                                              _("Enter your surname, please")})
    birthday = forms.DateField(input_formats=["%d.%m.%Y"], label=_("Birthday"),
                               required=False)
    bio = forms.CharField(widget=forms.Textarea(), label=_('Biography'),
                          required=False)
    email = forms.EmailField(max_length=50, widget=forms.TextInput(),
                             label=_("E-mail"), required=False)
    phone = forms.CharField(max_length=13, label=_('Phone'), required=False)
