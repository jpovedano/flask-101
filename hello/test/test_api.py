
import unittest
from flask import Flask

from hello.api import api

class RestClient(unittest.TestCase):

    def setUp(self):
        app = Flask(__name__)
        app.testing = True
        api.init_app(app)
        self.app = app

    def test_users_endpoint(self):
        with self.app.test_client() as client:
            response = client.get('/users')
            self.assertEqual(response.status_code, 200)

            response = client.get('/usrs')
            self.assertEqual(response.status_code, 404)


