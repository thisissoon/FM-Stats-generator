# Standard Libs
import datetime
import boto
import config

# Third Party Libs
import requests
from celery import app

# First Party Libs
from app.stats import pdf
from app.stats.pdf import template_factory


def get_monday(date):
    return date + datetime.timedelta(days=-date.weekday())


@app.task(name='weekly_stats')
def weekly_stats():
    today = datetime.date.today()
    (
        fetch_weekly_stats.s(get_monday(today).isoformat()) |
        generate_pdf_file.s(today.strftime('%V')) |
        upload_file_to_asw3.s('soonfm_stats.pdf') |
        send_email.s('email_weekly_stats.html')
    ).apply_async()


@app.task()
def fetch_weekly_stats(from_data):
    url = 'https://api.thisissoon.fm/player/stats?from={}'.format(from_data)
    return requests.get(url).json()


@app.task()
def generate_pdf_file(stats, week_num):
    return pdf.html2pdf(template_factory('weekly_stats.html').render(
        week_num=week_num, **stats)
    )


@app.task()
def upload_file_to_asw3(file_path, file_nane):
    s3 = boto.connect_s3(
        config.AWS_S3_ACCESS_KEY,
        config.AWS_S3_SECRET_KEY
    )
    bucket = s3.lookup(config.EXPORT_BUCKET_NAME)
    key = boto.s3.key.Key(bucket)
    key.key = file_nane
    key.set_contents_from_filename(file_path, policy='public-read')
    return key.generate_url(expires_in=0, query_auth=False)


@app.task()
def send_email(file_path, template):
    pass
