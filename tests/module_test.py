import time
import unittest

from simple_sum import sum_function


class TestStringMethods(unittest.TestCase):
    def test_isTrue(self):
        time.sleep(0.3)
        self.assertEqual(sum_function.sum_func(100, 20), 120)

    def test_isFalse(self):
        self.assertFalse(sum_function.sum_func(10, -6) == 5)

    def test_sum(self):
        self.assertTrue(sum_function.sum_func(10, -6) == 4)


if __name__ == "__main__":
    unittest.main()
