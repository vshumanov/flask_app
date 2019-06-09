import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import flask_app
from application.main.config import basedir


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        flask_app.config.from_object(
            'application.main.config.DevelopmentConfig')
        return flask_app

    def test_app_is_development(self):
        self.assertFalse(flask_app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(flask_app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            flask_app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' +
            os.path.join(basedir, 'flask_app_main.db')
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        flask_app.config.from_object('application.main.config.TestingConfig')
        return flask_app

    def test_app_is_testing(self):
        self.assertFalse(flask_app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(flask_app.config['DEBUG'])
        self.assertTrue(
            flask_app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///' +
            os.path.join(basedir, 'flask_app_test.db')
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        flask_app.config.from_object(
            'application.main.config.ProductionConfig')
        return flask_app

    def test_app_is_production(self):
        self.assertTrue(flask_app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
