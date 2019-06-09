import datetime
import unittest

from application.main import db
from application.main.model.contact import Contact
from application.main.service.contact_service import (get_all_contacts, get_contact,
                                                      save_new_contact, update_contact, delete_contact)
from application.test.base import BaseTestCase


class TestContactService(BaseTestCase):
    test_contact = {
        'emails': ['test1@test.com', 'test2@test.com'],
        'username': 'test',
        'first_name': 'test',
        'surname': 'test'
    }

    updated_contact = {
        'emails': ['test1_up@test.com', 'test2_up@test.com'],
        'username': 'test_up',
        'first_name': 'test_up',
        'surname': 'test_up'
    }

    def test_create_contact(self):

        response, code = save_new_contact(self.test_contact)

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(code, 201)
        self.assertEqual(response['status'], 'success')

    def test_get_all(self):
        response = get_all_contacts()
        self.assertTrue(isinstance(response, list))

    def test_get_contact(self):
        save_new_contact(self.test_contact)
        response = get_contact('test')
        self.assertTrue(isinstance(response, db.Model))
        self.assertEqual(response.username, 'test')

    def test_update_contact(self):
        save_new_contact(self.test_contact)
        response, code = update_contact(
            'test', self.updated_contact)
        self.assertTrue(isinstance(response, db.Model))
        self.assertEqual(code, 200)
        self.assertEqual(response.as_dict(), self.updated_contact)

    def test_delete_contact(self):
        save_new_contact(self.test_contact)
        response, code = delete_contact('test')
        self.assertEqual(code, 200)
        self.assertTrue(isinstance(response, dict))
        self.assertEqual(response['status'], 'success')


if __name__ == '__main__':
    unittest.main()
