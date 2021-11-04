class Mammal:
    _kingdom = 'animals'

    def __init__(self, name, animal_type, sound):
        self.name = name
        self.type = animal_type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return self._kingdom.capitalize()

    def info(self):
        return f'{self.name} is of type {self.type}'


class Tiger(Mammal):
    _kingdom = 'tigers'


mammal = Tiger("Tiger", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
