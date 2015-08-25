# Third Party Libs
from celery import app


@app.task(name='weekly_stats')
def weekly_stats():
    pass
