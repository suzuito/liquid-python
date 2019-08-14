from unittest import TestCase
from liquidcli.client import Client, DEFAULT_REQUEST_HEADERS
from liquidcli.data import Page, Order
from dataclasses import dataclass
from typing import Mapping, List, Callable
from dataclasses import dataclass

from util import assertHTTPRequest, Case


class TestGetOrders(TestCase):
    def test(self):
        testCases: List[Case] = [
            Case(
                desc='success',
                runner=lambda cli: cli.getOrders(),
                reqMethod='get',
                reqPath='/orders',
                resStatus=200,
                resBody='''
                {
                    "current_page": 1,
                    "total_pages": 999,
                    "models": [
                        {
                            "id": 100,
                            "order_type": "limit",
                            "side": "buy",
                            "price": 100.100,
                            "quantity": 0.01
                        }
                    ]
                }
                ''',
                expected=Page(
                    current_page=1, total_pages=999,
                    models=[
                        Order(
                            id=100,
                            order_type='limit',
                            side='buy',
                            price=100.100,
                            quantity=0.01,
                        ),
                    ],
                ),
            ),
        ]
        for tc in testCases:
            with self.subTest(desc=tc.desc):
                assertHTTPRequest(
                    self,
                    tc.reqMethod,
                    tc.reqPath,
                    tc.reqParams,
                    tc.reqData,
                    DEFAULT_REQUEST_HEADERS,
                    tc.resStatus,
                    tc.resBody,
                    tc.runner,
                    tc.expected,
                    tc.expectedErrMsg,
                )
