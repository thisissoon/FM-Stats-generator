from __future__ import absolute_import

# Third Party Libs
import config
from celery import Celery
from celery.utils.log import get_task_logger


app = Celery(
    name=__name__,
)

app.config_from_object(config.celery)
logger = get_task_logger(__name__)
