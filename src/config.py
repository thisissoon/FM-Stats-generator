# Standard Libs
import os
from datetime import timedelta


FM_API_URL = os.environ.get('FM_API_URL')


AWS_S3_ACCESS_KEY = os.environ.get('AWS_S3_ACCESS_KEY')
AWS_S3_SECRET_KEY = os.environ.get('AWS_S3_SECRET_KEY')
EXPORT_BUCKET_NAME = os.environ.get('EXPORT_BUCKET_NAME')


class Celery(object):
    BROKER_URL = os.environ.get('BROKER_URI')
    CELERY_RESULT_BACKEND = os.environ.get('BROKER_URI')
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERYBEAT_SCHEDULE = {
        'weekly_stats': {
            'task': 'weekly_stats',
            'schedule': timedelta(minutes=1),
            'args': [],
        }
    }

celery = Celery()
