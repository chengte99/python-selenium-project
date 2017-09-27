import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_case(self):
        a = "Hello, world"
        b = "Hello"
        self.assertIn(b, a, msg='a is not contain b')

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()
