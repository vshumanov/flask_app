import datetime
import unittest
import json

from manage import flask_app


from application.test.base import BaseTestCase
from application.main.model.contact import Contact


class TestContactAPI(BaseTestCase):
    test_contact = {
        'emails': ['test1@test.com', 'test2@test.com'],
        'username': 'test',
        'first_name': 'test',
        'surname': 'test'
    }

    updated_contact = {
        'emails': ['test_up@test.com'],
        'username': 'test_up',
        'first_name': 'test_up',
        'surname': 'test_up'
    }

    def test_api_get_all(self):
        resp = self.test_cl.get('/contact')
        self.assertEqual(resp.status_code, 200)

    def test_api_get_one(self):
        resp = self.test_cl.get('/contact/test')
        self.assertEqual(resp.status_code,  404)

    def test_api_post_contact(self):
        resp = self.test_cl.post(
            '/contact', data=json.dumps(self.test_contact), headers={'content-type': 'application/json'})
        self.assertEqual(resp.status_code, 201)

    def test_api_put_contact(self):
        resp = self.test_cl.put(
            '/contact/test', data=json.dumps(self.updated_contact), headers={'content-type': 'application/json'})
        self.assertEqual(resp.status_code, 404)

    def test_api_delete_contact(self):
        resp = self.test_cl.delete(
            '/contact/test', data=json.dumps(self.updated_contact), headers={'content-type': 'application/json'})
        self.assertEqual(resp.status_code, 404)


if __name__ == '__main__':
    unittest.main()
