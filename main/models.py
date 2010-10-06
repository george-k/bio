# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Contact(models.Model):
    """ Contact info class """

    name = models.CharField(max_length=50, verbose_name=_('name'))
    surname = models.CharField(max_length=50, verbose_name=_('surname'))
    birthday = models.DateField(blank=True, null=True,
                                verbose_name=_('birthday'))
    bio = models.TextField(blank=True, verbose_name=_('biography'))
    email = models.CharField(max_length=50, blank=True,
                            verbose_name=_("e-mail"))
    phone = models.CharField(max_length=13, blank=True,
                             verbose_name=_('phone'))

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)
