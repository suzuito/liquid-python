from unittest import TestCase
from liquidcli.client import Client, DEFAULT_REQUEST_HEADERS
from liquidcli.data import Page, Order
from dataclasses import dataclass
from typing import Mapping, List, Callable
from dataclasses import dataclass

from util import assertHTTPRequest, Case


class TestCancelOrders(TestCase):
    def test(self):
        testCases: List[Case] = [
            Case(
                desc='success',
                runner=lambda cli: cli.cancelOrders(
                    id=5,
                ),
                reqMethod='put',
                reqPath='/orders/5/cancel',
                resStatus=200,
                resBody='''
                {
                    "id": 1,
                    "order_type": "limit"
                }
                ''',
                expected=Order(
                    id=1,
                    order_type='limit',
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
