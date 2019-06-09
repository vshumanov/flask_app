from flask_testing import TestCase

from application.main import db
from manage import flask_app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        flask_app.config.from_object('application.main.config.TestingConfig')
        return flask_app

    def setUp(self):
        self.test_cl = flask_app.test_client()
        db.create_all()
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
