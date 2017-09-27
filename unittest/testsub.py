from calculator import Count
import unittest

class TestSub(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_sub1(self):
        result = Count(8, 4).sub()
        self.assertEqual(result, 4, msg='result is not equal 4')

    def test_sub2(self):
        result = Count(7, 4).sub()
        self.assertEqual(result, 3, msg='result is not equal 3')

    def tearDown(self):
        print("test end")

if __name__ == '__main__':
    unittest.main()
