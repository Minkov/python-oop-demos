from project.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    __DEFAULT_PORTION_SIZE = 200

    def __init__(self, name, price):
        super().__init__(name, self.__DEFAULT_PORTION_SIZE, price)
