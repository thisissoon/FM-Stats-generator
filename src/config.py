# Standard Libs
import os
from datetime import timedelta


FM_API_URL = os.environ.get('FM_API_URL')


class Celery(object):
    BROKER_URL = os.environ.get('RABBITMQ_URI')
    CELERY_RESULT_BACKEND = os.environ.get('RABBITMQ_URI')
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERYBEAT_SCHEDULE = {
        'producer': {
            'task': 'producer',
            'schedule': timedelta(minutes=1),
            'args': [],
        }
    }

celery = Celery()
