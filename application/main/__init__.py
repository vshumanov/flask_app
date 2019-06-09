from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from celery import Celery


from .config import config_by_name, CeleryConfig

db = SQLAlchemy()


def make_celery(flask_app):
    # create context tasks in celery
    celery_app = Celery('tasks')
    celery_app.config_from_object(CeleryConfig)
    flask_app.app_context().push()

    TaskBase = celery_app.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with flask_app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery_app.Task = ContextTask
    return celery_app


def create_app(config_name):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_by_name[config_name])

    flask_app.url_map.strict_slashes = False
    db.init_app(flask_app)

    return flask_app
