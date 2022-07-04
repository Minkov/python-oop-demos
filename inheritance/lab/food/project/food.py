from time import strptime


class Food:
    def __init__(self, expiration_date):
        self.expiration_date = expiration_date
        # self.expiration_date_as_date = strptime(expiration_date, '%d/%m/%y')
