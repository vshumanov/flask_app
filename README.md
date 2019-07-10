# flask_app


    python manage.py db update - apply db migrations

    python manage.py test - run tests

    python manage.py run - run app

# swagger 
    available at localhost:5000/ by default

# celery tasks

worker 
    
    celery -A manage.celery_app worker -l info

beat

    celery -A manage.celery_app beat -l debug
