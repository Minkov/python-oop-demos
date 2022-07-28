import unittest
from unittest import TestCase
from unittest.mock import patch, MagicMock, Mock

from app.person import Person

# Triple A - Arrange, Act, Assert
from app.validators.name_validator import ValidationException

counter = 0


class TestPerson(TestCase):
    FIRST_NAME = '1'
    LAST_NAME = '1'
    AGE = 19

    @classmethod
    def setUpClass(cls) -> None:
        """
        Runs **once before** all tests
        :return:
        """
        pass

    def setUp(self) -> None:
        """
        Runs **before** each test
        :return:
        """

    def tearDown(self) -> None:
        """
        Runs **after** each test
        :return:
        """
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Runs **once after** all tests
        :return:
        """
        pass

    def test_get_info__expect_to_be_correct(self):
        """
               `act__arrange__assert` for test naming
               """
        # Arrange
        # Act
        self.person = Person(self.FIRST_NAME, self.LAST_NAME, self.AGE)
        actual_info = self.person.get_info()
        expected_info = f'My name is {self.FIRST_NAME} {self.LAST_NAME} and I am {self.AGE}-years-old!'

        self.assertEqual(expected_info, actual_info)

    @patch('app.validators.name_validator.validate_name')
    def test_fullname__when_names_are_valid__expect_to_be_correct(self, _):
        self.person = Person('1', '1', 19)
        actual_fullname = self.person.fullname

        # Assert
        expected_fullname = f'{self.FIRST_NAME} {self.LAST_NAME}'
        self.assertEqual(expected_fullname, actual_fullname)

    @patch('app.validators.name_validator.validate_name')
    def test_init__when_first_name_is_invalid_expect_to_raise(self, mock_validate_name):
        mock_validate_name.side_effect = Mock(side_effect=ValidationException('First name invalid'))
        with self.assertRaises(ValidationException) as context:
            Person('Doncho', 'Minkov', 19)

        print(context.exception)

        self.assertIsNotNone(context.exception)

    @patch('app.validators.name_validator.validate_name')
    def test_init__when_last_name_is_invalid_expect_to_raise(self, mock_validate_name):
        mock_validate_name.side_effect = Mock(side_effect=ValidationException('Last name invalid'))

        with self.assertRaises(ValidationException) as context:
            Person('Doncho', 'Minkov', 19)

        print(context.exception)

        self.assertIsNotNone(context.exception)


if __name__ == '__main__':
    unittest.main()
