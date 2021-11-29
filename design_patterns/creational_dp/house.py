from utils import StrDictMixin


class LivingPlace:
    pass


class House(StrDictMixin, LivingPlace):
    def __init__(self, floors_count, has_garage, has_electricity, rooms_count, balconies_count, has_pool, town):
        self.floors_count = floors_count
        self.has_garage = has_garage
        self.has_electricity = has_electricity
        self.rooms_count = rooms_count
        self.balconies_count = balconies_count
        self.town = town
        self.has_pool = has_pool

    @classmethod
    def in_sofia(cls, floors_count, rooms_count, balconies_count):
        return cls(floors_count, False, True, rooms_count, balconies_count, False, 'Sofia')
