import unittest
from liquidcli import client


class Test_A(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aaa(self):
        self.assertEqual(2, 2)
        client.Client()
        pass
