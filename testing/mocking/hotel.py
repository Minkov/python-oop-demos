from mocking import rooms_manager


class Hotel2:
    def __init__(self, rooms_manager):
        self.rooms_manager = rooms_manager

    def book_a_room(self):
        if not self.rooms_manager.has_free_rooms():
            raise Exception('No free rooms')

        return self.rooms_manager.rooms.pop()


class Hotel:
    def __init__(self):
        self.rooms_manager = rooms_manager.RoomsManager([1, 2, 3])

    def book_a_room(self):
        if not self.rooms_manager.has_free_rooms():
            raise Exception('No free rooms')

        return self.rooms_manager.rooms.pop()
