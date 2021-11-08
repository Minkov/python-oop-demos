class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        hotel_name = f'{stars_count} stars Hotel'
        return cls(hotel_name)

    def _get_room_by_number(self, room_number):
        possible_rooms = [r for r in self.rooms if r.number == room_number]
        return possible_rooms[0]

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, guests_count):
        room = self._get_room_by_number(room_number)
        if room.take_room(guests_count):
            return

        self.guests += guests_count

    def free_room(self, room_number):
        room = self._get_room_by_number(room_number)

        if room.free_room():
            return

        self.guests -= room.guests

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f'''Hotel {self.name} has {self.guests} total guests
Free rooms: {', '.join(free_rooms)}
Taken rooms: {', '.join(taken_rooms)}'''
