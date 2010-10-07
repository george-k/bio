# -*- coding: utf-8 -*-
from django import template
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
    link = "/admin/{app}/{module}/{obj_pk}/".\
           format(app=object._meta.app_label,
                  module=object._meta.module_name,
                  obj_pk=object.pk)
    return link


