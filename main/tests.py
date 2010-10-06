# -*- coding: utf-8 -*-
from datetime import date
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


class TestContactEdit(HttpTestCase):
    """ Test contact edit form work """

    def contact_edit_test(self):
        #Prepare test data
        TEST_DATA = {'name': 'test_name',
                     'surname': 'test_surname',
                     'birthday': '01.01.2010',
                     'bio': 'test_bio',
                     'email': 'test@test.com',
                     'phone': '1234567890'
                     }
        #Send post request to edit contact
        response = self.client.post('/edit_contact/', TEST_DATA)
        #Get edited contact
        contact = Contact.objects.get(pk=1)
        #Check contact members with test dict fields
        self.assert_equal(contact.name, TEST_DATA['name'])
        self.assert_equal(contact.surname, TEST_DATA['surname'])
        self.assert_equal(contact.birthday.strftime("%d.%m.%Y"),
                          TEST_DATA['birthday'])
        self.assert_equal(contact.bio, TEST_DATA['bio'])
        self.assert_equal(contact.email, TEST_DATA['email'])
        self.assert_equal(contact.phone, TEST_DATA['phone'])
        
        
