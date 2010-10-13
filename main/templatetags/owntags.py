# -*- coding: utf-8 -*-
from django import template
from django.core import urlresolvers
from django.db.models.base import ModelBase


register = template.Library()


@register.simple_tag
def admin_link(object):
    """ Returns link for object admin edit page """
    try:
        if not object.__metaclass__ == ModelBase:
            raise
    except:
        err = "Admin_link tag argument must be " + \
              "a subclass of django.models.Model."
        raise template.TemplateSyntaxError(err)
    link = urlresolvers.reverse('admin:{app}_{model}_change'.\
                                format(app=object._meta.app_label,
                                       model=object._meta.module_name),
                                args=(object.id,))
    return link
