from server import app
from tests import unittest

class TestServer(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_root_route(self):
        response = self.app.get('/')
        self.assertEqual(response.data, 'Hello, World!')
