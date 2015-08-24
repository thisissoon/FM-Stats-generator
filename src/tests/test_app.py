import unittest
from app import create_app
from flask import url_for


class CommentModelTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_dummy(self):
        assert url_for('api.approve_comment') == 'http://http://localhost:5000/api/1.0/'
