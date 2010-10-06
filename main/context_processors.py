# -*- coding: utf-8 -*-
from django.conf import settings


def settings2context(request):
    return {'settings': settings}
