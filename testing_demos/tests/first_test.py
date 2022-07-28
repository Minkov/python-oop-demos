import unittest
from random import random
from unittest import TestCase


class FirstTests(TestCase):  # Test Suite
    def setUp(self) -> None:
        """
        Runs before each test
        """
        pass

    def test_assertEqual(self):  # TestCase
        self.assertEqual(1, 1)

    def test_assertTrue(self):
        self.assertTrue(True)

    def test_assertListEqual(self):
        self.assertListEqual([1, 2, 3], [1, 2, 3])

    def test_assertTrue2(self):
        self.assertTrue(False)

    def test_assertListEqual2(self):
        self.assertListEqual([1, 3], [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
