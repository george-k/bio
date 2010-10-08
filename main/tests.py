# -*- coding: utf-8 -*-
from datetime import date
from StringIO import StringIO
import sys

from django.conf import settings
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.template import Template, Context
from django.utils.simplejson import loads
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


class TestContactShow(HttpTestCase):
    """ Test main page with bio-data. """

    def contact_show_test(self):
        self.get200('/')
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
        #Login
        user = self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        #Fill and submit form
        self.go('/edit_contact/')
        for field in TEST_DATA:
            self.formvalue('1', field, TEST_DATA[field])
        self.submit('0')
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


class TestAuth(HttpTestCase):

    def test_login(self):
        self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        self.url(settings.LOGIN_REDIRECT_URL)

    def test_logout(self):
        self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        self.logout()
        self.url('/')


class TestAdminLink(HttpTestCase):
    """ Test tag, wich returns link to object admin edit page """

    def test_admin_link(self):
        contact = Contact.objects.get(pk=1)
        pattern = "/admin/{app}/{module}/{obj_pk}/".\
                  format(app=contact._meta.app_label,
                         module=contact._meta.module_name,
                         obj_pk=contact.pk)
        template = Template('{% load owntags %}{% admin_link contact %}')
        res = template.render(Context({'contact': contact}))
        self.assert_equal(res, pattern)


class TestPrintModelsCommand(HttpTestCase):
    """ Check output of 'print_models' command """

    def test_print_models_command(self):
        saveout = sys.stdout
        sys.stdout = output = StringIO()
        call_command('printmodels')
        sys.stdout = saveout
        self.assert_not_equal(output.getvalue().find('models found'), -1)
        self.assert_not_equal(output.getvalue().find('class'), -1)
        self.assert_not_equal(output.getvalue().find('object(s)'), -1)


class TestAjax(HttpTestCase):
    """ Test ajax form work """

    def test_ajax(self):
        #Login
        user = self.helper('create_user', 'testuser', 'password')
        self.login('testuser', 'password')
        #Send correct request and check it
        TEST_DATA = {'name': 'testname', 'surname': 'testsurname'}
        response = self.client.post('/edit_contact/', TEST_DATA,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        try:
            result = loads(response.content)
        except:
            self.assert_false(True, 'Not JSON response')
        self.assert_equal(result.get('result'), 'ok')
        #Send incorrect request and check it
        TEST_DATA = {'name': '', 'surname': ''}
        response = self.client.post('/edit_contact/', TEST_DATA,
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        try:
            result = loads(response.content)
        except:
            self.assert_false(True, 'Not JSON response')
        self.assert_equal(result.get('result'), 'error')


class TestLogsList(HttpTestCase):
    """ Test last request logs list """

    def test_logs_list(self):
        test_path = '/test_path/'
        self.client.get(test_path)
        response = self.client.get(reverse('last_logs'))
        self.assert_not_equal(response.content.find(test_path), -1)
