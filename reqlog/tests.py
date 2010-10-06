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
        self.client.get('/?testparam=logging')
        #Check apropriate request log
        try:
            RequestLog.objects.get(Q(path='/'),
                                   Q(req_str__contains='testparam'),
                                   Q(req_str__contains='logging'))
        except ObjectDoesNotExist:
            self.assert_false(True)
