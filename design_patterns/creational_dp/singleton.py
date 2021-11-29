from utils import StrDictMixin


def singleton(cls):
    instances = []

    def wrapper(*args, **kwargs):
        if not instances:
            instances.append(cls(*args, **kwargs))
        return instances[0]

    return wrapper


# @singleton
class House(StrDictMixin):
    def __init__(self, floors_count, has_pool):
        self.floors_count = floors_count
        self.has_pool = has_pool


# Combination of singleton & factory
# More practical Singleton
class HousesFactory:
    house_instance = House(3, False)

    def get_house(self):
        return self.house_instance


print(House(3, True))
print(House(2, False))
print(House(1, True) == House(2, False))

print(HousesFactory().get_house())
print(HousesFactory().get_house())
print(HousesFactory().get_house())
print(HousesFactory().get_house() == HousesFactory().get_house())
