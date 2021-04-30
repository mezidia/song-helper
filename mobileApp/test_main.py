from unittest import TestCase
import asyncio
import utils


class Test(TestCase):
    def setUp(self) -> None:
        self.expected = {'success': 'https://github.com/mezgoodle', 'failure': 'dadas@@@#ssf'}
        self.data = {'success': 'mezgoodle', 'failure': 'dadas@@@#ssf'}

    def test_make_request_success(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(utils.make_request(self.data['success']))
        self.assertEqual(result['html_url'], self.expected['success'])

    def test_make_request_failure(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(utils.make_request(self.data['failure']))
        self.assertFalse('html_url' in result)
