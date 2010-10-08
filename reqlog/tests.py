# -*- coding: utf-8 -*-
from tddspry.django import HttpTestCase
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from reqlog.models import RequestLog


class TestRequestLogging(HttpTestCase):
    """ Reques and check log existing """

    def test_request_logging(self):
        """ Check request logging """
        #Send request
        self.client.get('/test_path/?testparam=logging')
        #Check apropriate request log
        last_logs = RequestLog.objects.order_by('-date')[0:1]
        self.assert_true(len(last_logs), 'Log not found')
        last_log = last_logs[0]
        self.assert_not_equal(last_log.req_str.find('testparam'), -1)
        self.assert_not_equal(last_log.req_str.find('logging'), -1)
        self.assert_not_equal(last_log.path.find('test_path'), -1)
