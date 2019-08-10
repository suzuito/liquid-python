from unittest import TestCase
from liquidcli.client import DEFAULT_REQUEST_HEADERS
from liquidcli.data import Execution, Page

from util import assertHTTPRequest


class TestGetExecutions(TestCase):
    def test(self):
        testCases = [
            {
                'desc': 'success',
                'inputProductId': 1, 'inputLimit': 1, 'inputPage': 1,
                'resStatus': 200,
                'resBody': '''
                {
                    "current_page": 1,
                    "total_pages": 999,
                    "models": [
                        {
                            "id": 100,
                            "quantity": 0.01,
                            "price": 100.100,
                            "taker_side": "sell",
                            "created_at": 1
                        }
                    ]
                }
                ''',
                'expected': Page(
                    currentPage=1, totalPages=999,
                    models=[
                        Execution(
                            id=100,
                            quantity=0.01,
                            price=100.100,
                            taker_side='sell',
                            created_at=1,
                        ),
                    ],
                ),
            },
        ]
        for tc in testCases:
            with self.subTest(desc=tc['desc']):
                assertHTTPRequest(
                    self,
                    'get', '/executions',
                    {
                        'product_id': tc['inputProductId'],
                        'limit': tc['inputLimit'],
                        'page': tc['inputPage'],
                    },
                    None,
                    DEFAULT_REQUEST_HEADERS,
                    tc['resStatus'],
                    tc['resBody'],
                    lambda cli: cli.getExecutions(
                        tc['inputProductId'],
                        tc['inputLimit'],
                        tc['inputPage'],
                    ),
                    tc.get('expected', None),
                    tc.get('expectedErr', None),
                )


class TestGetExecutionsByTimestamp(TestCase):
    def test(self):
        testCases = [
            {
                'desc': 'success',
                'inputCPair': 'BTCJPY', 'inputLimit': 2, 'inputTimestamp': 3,
                'resStatus': 200,
                'resBody': '''
                [
                    {
                        "id": 100,
                        "quantity": 0.01,
                        "price": 100.100,
                        "taker_side": "sell",
                        "created_at": 1
                    }
                ]
                ''',
                'expected': [
                    Execution(
                        id=100,
                        quantity=0.01,
                        price=100.100,
                        taker_side='sell',
                        created_at=1,
                    ),
                ],
            },
        ]
        for tc in testCases:
            with self.subTest(desc=tc['desc']):
                assertHTTPRequest(
                    self,
                    'get', '/executions',
                    {
                        'currency_pair_code': tc['inputCPair'],
                        'timestamp': tc['inputTimestamp'],
                        'limit': tc['inputLimit'],
                    },
                    None,
                    DEFAULT_REQUEST_HEADERS,
                    tc['resStatus'],
                    tc['resBody'],
                    lambda cli: cli.getExecutionsByTimestamp(
                        tc['inputCPair'],
                        tc['inputTimestamp'],
                        tc['inputLimit'],
                    ),
                    tc.get('expected', None),
                    tc.get('expectedErr', None),
                )
