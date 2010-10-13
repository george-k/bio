# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from tddspry.django import HttpTestCase

from main.models import Contact
from reqlog.models import RequestLog, ObjectActionLog


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

    def test_priority_field(self):
        """ Check log priority field """
        #Send request
        self.client.get('/test_path/?teststring')
        #Check last log priority
        #(must be priority member and it must be equal to default value)
        last_logs = RequestLog.objects.order_by('-date')[0:1]
        self.assert_true(len(last_logs), 'Log not found')
        last_log = last_logs[0]
        self.assert_not_equal(last_log.req_str.find('teststring'), -1)
        self.assert_equal(last_log.priority, 0, 'Request log priority failed')


class TestObjectActionLogging(HttpTestCase):
    """ Check object action log record creation """

    def test_object_creation_logging(self):
        contact = Contact(name="testname", surname="testsurname")
        contact.save()
        last_log = ObjectActionLog.objects.order_by('-date')[0]
        self.assert_not_equal(last_log.model.find('Contact'), -1)
        self.assert_equal(last_log.object_pk, str(contact.pk))
        self.assert_equal(last_log.action, 'created')

    def test_object_updating_logging(self):
        contact = Contact(name="testname", surname="testsurname")
        contact.save()
        contact.bio = "testbio"
        contact.save()
        last_log = ObjectActionLog.objects.order_by('-date')[0]
        self.assert_not_equal(last_log.model.find('Contact'), -1)
        self.assert_equal(last_log.object_pk, str(contact.pk))
        self.assert_equal(last_log.action, 'updated')

    def test_object_deleting_logging(self):
        contact = Contact(name="testname", surname="testsurname")
        contact.save()
        contact_pk = contact.pk
        contact.delete()
        last_log = ObjectActionLog.objects.order_by('-date')[0]
        self.assert_not_equal(last_log.model.find('Contact'), -1)
        self.assert_equal(last_log.object_pk, str(contact_pk))
        self.assert_equal(last_log.action, 'deleted')
