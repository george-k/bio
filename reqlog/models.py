# -*- coding: utf-8 -*-
from django.contrib.admin.models import LogEntry
from django.db import models
from django.db.models.signals import post_save, post_delete
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
    priority = models.PositiveIntegerField(verbose_name=_('priority'),
                                           default=0)

    class Meta:
        verbose_name = _('request log')
        verbose_name_plural = _('request logs')

    def __unicode__(self):
        return self.path


class ObjectActionLog(models.Model):
    """ Commit every object creation/updating/deleting for project models """

    ACTIONS = (
        ('created', _('Created')),
        ('updated', _('Updated')),
        ('deleted', _('Deleted')),
    )

    date = models.DateTimeField(auto_now_add=True, verbose_name=_('date'))
    model = models.CharField(max_length=150, verbose_name=_('model name'))
    object_pk = models.CharField(max_length=10, verbose_name=_('object pk'))
    action = models.CharField(max_length=30, choices=ACTIONS,
                              verbose_name=_('action'))

    class Meta:
        verbose_name = _('object action log')
        verbose_name_plural = _('object actions log')

    def __unicode__(self):
        return "%s %s : %s" % (self.model, self.object_pk, self.action)


def object_action_log(sender, **kwargs):
    """ Handle every object action and make new log record """
    #Exclude logging models
    if sender in (RequestLog, ObjectActionLog, LogEntry):
        return
    #Make new log record
    new_log = ObjectActionLog(model=str(sender),
                              object_pk=kwargs['instance'].pk)
    if 'created' in kwargs:
        new_log.action = 'created' if kwargs['created'] else 'updated'
    else:
        new_log.action = 'deleted'
    new_log.save()


post_save.connect(object_action_log)
post_delete.connect(object_action_log)
