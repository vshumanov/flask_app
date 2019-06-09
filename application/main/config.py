import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))
# windows and celery dont like eachother
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'flask_app_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PORT = 5000


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, 'flask_app_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    PORT = 8080


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)


# Create Celery beat schedule:
celery_push_contact_schedule = {
    'push_contact_15_sec': {
        'task': 'tasks.periodic_run_push_contact',
        'schedule': timedelta(seconds=15),
    },
    'delete_all_every_minute': {
        'task': 'tasks.periodic_run_delete_last_minute',
        'schedule': timedelta(seconds=60)
    }
}


# TODO add test and prod conf for celery
class CeleryConfig():
    beat_schedule = celery_push_contact_schedule
    broker_url = 'redis://localhost:6379/0'
    result_backend = 'redis://localhost:6379/0'
    redis_host = 'localhost'
    redis_password = ''
    redis_port = 6379
    redis_url = 'redis://localhost:6379/0'
    include = ['application.main.tasks']


key = Config.SECRET_KEY
