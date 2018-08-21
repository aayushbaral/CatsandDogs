import os
import unittest
from flaskapp import app

class UnitTest(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
if __name__ == '__main__':
    unittest.main()