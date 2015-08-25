# Standard Libs
import datetime
import json

# Third Party Libs
import httplib
from mock import patch

# First Party Libs
from app.tasks import fetch_weekly_stats, generate_pdf_file


class MockRequestsResponse(object):

    def __init__(self, resp_data, code=httplib.OK, msg='OK'):
        self.resp_data = resp_data
        self.code = code
        self.msg = msg
        self.headers = {'content-type': 'application/json; charset=utf-8'}

    @property
    def text(self):
        return self.resp_data

    @property
    def status_code(self):
        return self.code

    def json(self):
        return json.loads(self.resp_data)


response_data = open('tests/resources/response_payload.json').read()


@patch('requests.get', return_value=MockRequestsResponse(response_data))
def test_fetch_weekly_stats(requests_get):
    today = datetime.date.today()
    assert isinstance(fetch_weekly_stats(today), dict)


def test_populate_pdf_with_data():
    generate_pdf_file(json.loads(response_data), 23)
