class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def has_capacity(self, guests_count):
        return guests_count <= self.capacity

    def take_room(self, guests_count):
        if self.is_taken or \
                not self.has_capacity(guests_count):
            return f'Room number {self.number} cannot be taken'

        self.is_taken = True
        self.guests = guests_count

    def free_room(self):
        if not self.is_taken:
            return f'Room number {self.number} is not taken'

        self.is_taken = False
        self.guests = 0


class Suite(Room):
    def __init__(self, number, rooms):
        super().__init__(number, sum(r.capacity for r in rooms))
        self.rooms = rooms

    def has_capacity(self, guests_count):
        pass
