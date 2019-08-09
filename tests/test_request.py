from unittest import TestCase
from liquidcli.client import Client
from requests import Response, Session

from util import BASE_URL, assertHTTPRequest


class TestRequest(TestCase):
    def testHTTPError(self):
        testCases = [
            (404, '404 Client Error'),
            (500, '500 Server Error'),
        ]
        for tc in testCases:
            self.subTest(code=tc[0])
            assertHTTPRequest(
                self, 'get', '/',
                {}, None, {},
                tc[0], 'Dummy',
                lambda cli: cli.getExecutions(1, 1, 1),
                {}, tc[1],
            )
