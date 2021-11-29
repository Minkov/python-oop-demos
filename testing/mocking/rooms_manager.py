class RoomsManager:
    def __init__(self, rooms):
        self.rooms = rooms

    def has_free_rooms(self):
        return any(self.rooms)
