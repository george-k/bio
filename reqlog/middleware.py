# -*- coding: utf-8 -*-
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
            log.req_str = "POST: %s GET: %s" % (request.POST, request.GET)
        except:
            pass
        log.save()
