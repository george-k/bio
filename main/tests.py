# -*- coding: utf-8 -*-
from tddspry.django import DatabaseTestCase, HttpTestCase
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

