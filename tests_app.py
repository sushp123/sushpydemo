import unittest
from unittest.mock import patch # for Python >= 3.3 use unittest.mock
from app import get_data, fetch_words


class MyTestCase(unittest.TestCase):
    def test_returns_true_if_url_found(self):
        with patch('requests.get') as mock_request:
            url = "https://www.gutenberg.org/files/2701/2701-0.txt"

            # set a `status_code` attribute on the mock object
            # with value 200
            mock_request.return_value.status_code = 200

            self.assertTrue(get_data(url))

    def test_fetch_words_none(self):
        data = None
        result = fetch_words(data)
        self.assertEqual(result, None)

    def test_fetch_words(self):
        data = "The Project Gutenberg eBook of Moby-Dick; or The Whale, by Herman Melville"
        result = fetch_words(data)
        self.assertEqual(result[0][0], "project")
        self.assertEqual(result[0][1], 1)


if __name__ == '__main__':
    unittest.main()
