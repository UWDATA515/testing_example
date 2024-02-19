import unittest
from unittest import mock

from google.doodle import load_google_doodle_title


class DoodleTest(unittest.TestCase):

    # The following line marks the requests.get function for mocking, which
    # means that you can access the mock version of the function as an
    # argument to the test function - `mock_get` below.
    @mock.patch('requests.get')
    def test_doodle_response_with_doodle(self, mock_get):
        mock_response = mock.Mock(status_code=200)
        mock_response.text = """<!doctype html><html><meta content="Valentine's Day 2024" property="twitter:title"><meta content="Happy Valentine's Day! #GoogleDoodle" property="twitter:description"></html>"""
        mock_get.return_value = mock_response

        title = load_google_doodle_title()
        self.assertEqual(title, "Valentine's Day 2024")


if __name__ == '__main__':
    unittest.main()