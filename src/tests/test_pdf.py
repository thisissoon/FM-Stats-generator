# First Party Libs
from app.stats.pdf import template_factory, html2pdf
import json
import os

data = json.loads(open('tests/resources/response_payload.json').read())


def test_template_factory():
    assert len(template_factory('weekly_stats.html').render(**data))


def test_html2pdf():
    fle = html2pdf(template_factory('weekly_stats.html').render(**data))
    assert os.path.getsize(fle)
