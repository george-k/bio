# -*- coding: utf-8 -*-
from django.utils.simplejson import dumps

from reqlog.models import RequestLog


class RequestLoggingMiddleware:

    def process_request(self, request):
        """ Create log for request """

        #Exclude requests from admin
        if 'admin' in request.path:
            return

        log = RequestLog()
        log.path = request.path
        log.method = request.method
        try:
            log.remote_address = request.META['REMOTE_ADDR']
        except:
            pass
        try:
            log.referer = request.META['HTTP_REFERER']
        except:
            pass
        try:
            log.remote_host = request.META['REMOTE_HOST']
        except:
            pass
        try:
            log.user_agent = request.META['HTTP_USER_AGENT']
        except:
            pass
        try:
            log.is_sequre = request.is_sequre()
        except:
            pass
        try:
            res = {'POST': dict(request.POST)}
            res.update({'GET': dict(request.GET)})
            log.req_str = dumps(res, ensure_ascii=False, sort_keys=True)
        except:
            pass
        log.save()
