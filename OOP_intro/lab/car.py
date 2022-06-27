class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

name = 'Kia'
model = 'Rio'
engine = '1.3L B3 I4'


def get_info():
    return f'This is {name} {model} with engine {engine}'
