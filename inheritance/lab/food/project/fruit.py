from project.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        # self.expiration_date = expiration_date  # This is wrong.
        super().__init__(expiration_date)  # This is the correct way
        self.name = name
