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
        self.client.get('/?testparam=logging')
        #Check apropriate request log
        try:
            RequestLog.objects.get(Q(path='/'),
                                   Q(req_str__contains='testparam'),
                                   Q(req_str__contains='logging'))
        except ObjectDoesNotExist:
            self.assert_false(True)


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
