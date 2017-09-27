from count import is_prime
import unittest

class Test(unittest.TestCase):

    def setUp(self):
        print("test start")

    def test_is_prime(self):
        self.assertTrue(is_prime(8), msg='8 is not prime')

    def tearDown(self):
        print("test end")

if __name__ == "__main__":
    unittest.main()
