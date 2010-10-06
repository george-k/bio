# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


class RequestLog(models.Model):
    """ HTTP request log entry """

    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    path = models.CharField(max_length=255, verbose_name=_('path'))
    method = models.CharField(max_length=255, verbose_name=_('HTTP method'))
    remote_address = models.IPAddressField(blank=True, null=True,
                                           verbose_name=_('remote address'))
    referer = models.CharField(max_length=255, blank=True, null=True,
                               verbose_name=_('referer'))
    remote_host = models.CharField(max_length=255, blank=True, null=True,
                                   verbose_name=_('remote host'))
    user_agent = models.CharField(max_length=255, blank=True, null=True,
                                  verbose_name=_('user agent'))
    is_sequre = models.BooleanField(verbose_name=_('is sequre'), default=False)
    req_str = models.TextField(blank=True,  null=True,
                               verbose_name=_('request string'))

    class Meta:
        verbose_name = _('request log')
        verbose_name_plural = _('request logs')

    def __unicode__(self):
        return self.path
