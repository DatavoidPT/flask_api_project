import unittest
from app import APP


class AppTests(unittest.TestCase):

    def setUp(self):
        """
           The setUp method is used will be used to construct all our test
        """

        self.app = APP
        self.client = self.app.test_client()

    def test_app(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()