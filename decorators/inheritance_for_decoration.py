class Person:
    pass


class Car:
    pass


class Dog:
    pass


class CarPerson(Person, Car):
    pass


class PersonDog(Person, Dog):
    pass


class CarPersonDog(Car, Person, Dog):
    pass
