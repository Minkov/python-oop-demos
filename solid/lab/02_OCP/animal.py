class Animal:
    _sound = None
    _species = None

    def get_species(self):
        return self._species

    def get_sound(self):
        return self._sound


class Cat(Animal):
    _sound = 'meow'
    _species = 'cat'


class Dog(Animal):
    _sound = 'woof-woof'
    _species = 'dog'


class Chicken(Animal):
    _sound = 'chik-chirik'
    _species = 'chicken'


class RobotChicken(Chicken):
    def get_sound(self):
        return 'Robot chicken makes a lot of noise'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Cat(), Dog(), Chicken()]
animal_sound(animals)
