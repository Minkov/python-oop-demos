from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    __DEFAULT_PORTION_SIZE = 245

    def __init__(self, name, price):
        super().__init__(name, self.__DEFAULT_PORTION_SIZE, price)
