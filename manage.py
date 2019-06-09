
import os
import unittest
import sys

from application.main import create_app, db, make_celery
from application.main.model import contact
from application import blueprint

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# FIX kinda hacky
sys.path.insert(0, 'D:\\flask_app')


flask_app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
flask_app .register_blueprint(blueprint)
celery_app = make_celery(flask_app)

flask_app.app_context().push()

manager = Manager(flask_app)

migrate = Migrate(flask_app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    """run the app"""
    flask_app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('application/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
