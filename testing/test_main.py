import unittest
from unittest import TestCase

from main import add


# inherit TestCase
class MainTest(TestCase):
    # test methods MUST start with `test`
    def test_add__when_1_and_2__expect_3(self):
        # arrange
        expected = 3

        # act
        actual = add(1, 2)

        # assert
        self.assertEqual(expected, actual)

    def test_add__when_2_and_1__expect_3(self):
        expected = 3
        actual = add(2, 1)
        self.assertEqual(expected, actual)

    def test_add__when_None_and_int__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            pass


if __name__ == '__main__':
    unittest.main()
