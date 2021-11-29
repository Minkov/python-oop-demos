from unittest import TestCase
from unittest.mock import patch, MagicMock

from mocking.hotel import Hotel, Hotel2


class HotelTests(TestCase):
    def test_book_a_room__when_no_free_rooms__expect_exception(self):
        hotel = Hotel()
        hotel.book_a_room()
        hotel.book_a_room()
        hotel.book_a_room()

        with self.assertRaises(Exception):
            hotel.book_a_room()

    @patch('mocking.rooms_manager.RoomsManager')
    def test_book_a_room__when_no_free_rooms__expect_exception_WITH_MOCKS(self, mock):
        RoomsManagerMock = mock.return_value
        RoomsManagerMock.has_free_rooms.return_value = False

        hotel = Hotel()
        with self.assertRaises(Exception):
            hotel.book_a_room()

        RoomsManagerMock.has_free_rooms.assert_called_once()

    def test_book_a_room__when_no_free_rooms__expect_exception_WITH_MOCKS_AND_DI(self):
        rooms_manager = MagicMock()
        rooms_manager.has_free_rooms.return_value = False
        hotel = Hotel2(rooms_manager)

        with self.assertRaises(Exception):
            hotel.book_a_room()

        rooms_manager.has_free_rooms.assert_called_once()
