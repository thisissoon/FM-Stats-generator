from __future__ import absolute_import

# Standard Libs
import config

# Third Party Libs
from celery import Celery
from celery.utils.log import get_task_logger


app = Celery(
    name=__name__,
)


app.config_from_object(config.celery)
logger = get_task_logger(__name__)
