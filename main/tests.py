# -*- coding: utf-8 -*-
from tddspry.django import DatabaseTestCase, HttpTestCase
from django.core.urlresolvers import reverse
from main.models import Contact


CONTACT_NAME = 'test_name'
CONTACT_NEW_NAME = 'new_name'


class TestContact(DatabaseTestCase):
    """ Make CRUD tests for Contact model """

    def create_test(self):
        self.assert_create(Contact, name=CONTACT_NAME)

    def delete_test(self):
        contact = self.assert_create(Contact, name=CONTACT_NAME)
        self.assert_delete(contact)

    def read_test(self):
        self.assert_create(Contact, name=CONTACT_NAME)
        self.assert_read(Contact, name=CONTACT_NAME)

    def update_test(self):
        contact = self.assert_create(Contact, name=CONTACT_NAME)
        self.assert_update(contact, name=CONTACT_NEW_NAME)


class TestContactShow(HttpTestCase):
    """ Test main page with bio-data. """

    def contact_show_test(self):
        res = self.get200('/')
        self.find('Name')
        self.find('Surname')
        self.find('Birthday')
        self.find('Biography')
        self.find('Phone')
        self.find('E-mail')


class TestRequestContext(HttpTestCase):
    """ Check django.settings in request context """

    def test_context(self):
        response = self.client.get('/')
        self.assert_true('settings' in response.context[0],
                         'No settings in context.')
