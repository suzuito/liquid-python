import unittest


class Test_A(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_aaa(self):
        self.assertEqual(2, 2)
        pass


if __name__ == '__main__':
    unittest.main()
