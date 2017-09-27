from calculator import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add1(self):
        result = Count(3, 4).add()
        self.assertEqual(result, 8, msg='result is not equal 8')

    def test_add2(self):
        result = Count(7, 4).add()
        self.assertEqual(result, 11, msg='result is not equal 11')

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()
