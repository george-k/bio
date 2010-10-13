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
        log.remote_address = request.META.get('REMOTE_ADDR')
        log.referer = request.META.get('HTTP_REFERER')
        log.remote_host = request.META.get('REMOTE_HOST')
        log.user_agent = request.META.get('HTTP_USER_AGENT')
        try:
            log.is_sequre = request.is_sequre()
        except:
            pass
        res = {'POST': dict(request.POST)}
        res.update({'GET': dict(request.GET)})
        log.req_str = dumps(res, ensure_ascii=False, sort_keys=True)
        log.save()
