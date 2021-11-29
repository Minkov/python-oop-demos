# house with 1 floor, no garage, no pool, electricity, 3 rooms, no balconies, sofia, no pool
from abc import ABC, abstractmethod

from creational_dp.house import House, LivingPlace


# Pros of Factories:
# - Easier way to create objects
# - Abstraction over object creation

# Factory method
class HousesFactory:
    def get_no_pool_house(self, floors_count, has_garage, rooms_count, balconies_count, town):
        return House(floors_count, has_garage, True, rooms_count, balconies_count, False, town)


# Simple factory

class HousesFactoryBase(ABC):
    @abstractmethod
    def get_house(self, *args, **kwargs) -> House:
        pass


class HousesInSofiaFactory(HousesFactoryBase):
    def get_house(self, floors_count, rooms_count, balconies_count):
        return House(floors_count, False, True, rooms_count, balconies_count, False, 'Sofia')


class HouseWithoutPoolFactory(HousesFactoryBase):
    def get_house(self, floors_count, has_garage, rooms_count, balconies_count, town) -> House:
        return House(floors_count, has_garage, True, rooms_count, balconies_count, False, town)


# Abstract factory

class LivingPlaceFactoryBase(ABC):
    @abstractmethod
    def get_house(self, *args, **kwargs) -> LivingPlace:
        pass


class HoseInSofiaLivingPlaceFactory(LivingPlaceFactoryBase):
    def get_house(self, floors_count, rooms_count, balconies_count) -> LivingPlace:
        return House(floors_count, False, True, rooms_count, balconies_count, False, 'Sofia')


house1 = House(1, False, False, 3, 0, False, 'Sofia')
house2 = House(1, False, False, 3, 0, False, None)

factory = HousesFactory()

print(factory.get_no_pool_house(3, True, 5, 2, 'Sofia'))
print(House.in_sofia(3, 5, 3))

print(HousesInSofiaFactory().get_house(3, 6, 19))
