import unittest
from server import app

class TestAppService(unittest.TestCase):
    """ App Server Tests """

    def setUp(self):
        """ Runs before each test """
        self.app = app.test_client()

    def test_index(self):
        """ Test the Home Page """
        resp = self.app.get("/")
        self.assertEqual(resp.status_code, 200)
        data = resp.get_data(as_text=True)
        self.assertEqual(data, "Hello, World!")

if __name__ == "__main__":
    unittest.main()
