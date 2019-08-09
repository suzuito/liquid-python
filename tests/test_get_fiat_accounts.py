from unittest import TestCase
from liquidcli.client import DEFAULT_REQUEST_HEADERS
from liquidcli.data import FiatAccount

from util import assertHTTPRequest


class TestGetFiatAccounts(TestCase):
    def test(self):
        testCases = [
            {
                'desc': 'success',
                'resStatus': 200,
                'resBody': '''
                [
                    {
                        "id": 1,
                        "currency": "JPY",
                        "currency_symbol": "¥",
                        "balance": 20.00,
                        "reserved_balance": 30.00,
                        "pusher_channel": "dummy001",
                        "lowest_offer_interest_rate": 40.00,
                        "highest_offer_interest_rate": 50.00,
                        "exchange_rate": 60.00,
                        "currency_type": "fiat"
                    }
                ]
                ''',
                'expected': [
                    FiatAccount(
                        id=1,
                        currency='JPY',
                        currency_symbol='¥',
                        balance=20.00, reserved_balance=30.00,
                        pusher_channel='dummy001',
                        lowest_offer_interest_rate=40.00,
                        highest_offer_interest_rate=50.00,
                        exchange_rate=60.00,
                        currency_type='fiat',
                    ),
                ],
            },
        ]
        for tc in testCases:
            with self.subTest(desc=tc['desc']):
                assertHTTPRequest(
                    self,
                    'get', '/fiat_accounts',
                    None,
                    None,
                    DEFAULT_REQUEST_HEADERS,
                    tc['resStatus'],
                    tc['resBody'],
                    lambda cli: cli.getFiatAccounts(),
                    tc.get('expected', None),
                    tc.get('expectedErr', None),
                )
