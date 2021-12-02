from project.drink.drink import Drink


class Tea(Drink):
    __DEFAULT_PRICE = 2.5

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, self.__DEFAULT_PRICE, brand)
