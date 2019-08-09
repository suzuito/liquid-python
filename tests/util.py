from unittest import TestCase
from unittest.mock import patch
from requests import Response, Session
from liquidcli.client import Client


BASE_URL = 'http://example.com'
API_TOKEN_ID = 'dummyToken'
API_SECRET = 'dummySecret'


def dummyNuncer():
    return 'dummyNonce'


def assertHTTPRequest(
    t: TestCase,
    reqMethod: str, reqPath: str, reqParams: dict,
    reqData, reqHeaders: dict, resStatusCode: int, resBody, fn,
    expected, expectedErrMsg,
):
    with patch.object(Response, 'content', bytes(resBody, 'utf8')):
        res: Response = Response()
        res.status_code = resStatusCode
        with patch.object(Session, 'request') as req:
            req.return_value = res
            cli = Client(BASE_URL, API_TOKEN_ID, API_SECRET, dummyNuncer)
            actual = None
            try:
                actual = fn(cli)
            except IOError as actualErr:
                t.assertRegex(
                    str(actualErr),
                    expectedErrMsg,
                )
                return
            req.assert_called_once_with(
                reqMethod,
                '{0}{1}'.format(BASE_URL, reqPath),
                params=reqParams,
                data=reqData,
                headers=reqHeaders,
                cookies=None, files=None,
                auth=None, timeout=None,
                allow_redirects=True, proxies=None,
                hooks=None, stream=None,
                verify=None, cert=None,
                json=None,
            )
            t.assertEqual(
                expected,
                actual,
                # '\nExp:{0} \nAct:{1}'.format(
                #     vars(expected),
                #     vars(actual),
                # )
            )
