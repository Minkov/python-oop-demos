from app.lab.cat import Cat

import unittest


class CatTests(unittest.TestCase):
    NAME = 'Pepelyashka'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_increment(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test_eat__expect_fed_to_be_true(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_eat__when_fed_is_true__expect_to_raise(self):
        # Arrange
        self.cat.eat()

        # Assert
        with self.assertRaises(Exception) as context:
            self.cat.eat()  # Act

        self.assertIsNotNone(context)
        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep__when_fed_is_false__expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test_sleep__expect_sleepy_to_be_false(self):
        # Arrange
        self.cat.eat()

        # Act
        self.cat.sleep()

        # Assert
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
