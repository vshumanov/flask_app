from ..main import make_celery, create_app
from datetime import timedelta
from .util.randomization import generate_random_email, get_random_name
from .service.contact_service import save_new_contact, delete_all

celery_app = make_celery(create_app('dev'))


@celery_app.task(name='tasks.periodic_run_push_contact')
def run_push_contact():
    """pushes random contact"""

    cont = {
        'emails': [
            generate_random_email(), generate_random_email()
        ],
        'username': get_random_name(),
        'first_name': get_random_name(),
        'surname': get_random_name()
    }

    save_new_contact(cont)


@celery_app.task(name='tasks.periodic_run_delete_last_minute')
def run_delete_last_minute():
    """ deletes all contacts """
    print(f'deleted: {delete_all()}')
