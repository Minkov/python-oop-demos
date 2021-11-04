class Person:
    def __init__(self, name, age):
        self.x__name = name
        self.age = age

    def info(self):
        return f'Name: {self.x__name}, Age: {self.age}'

    def __generate_key(self, key):
        if key.startswith('x__'):
            return f'x__Person{key}'
        return key

    def __setattr__(self, key, value):
        super().__setattr__(self.__generate_key(key), value)

    def __getattr__(self, item):
        return super().__getattribute__(self.__generate_key(item))


p = Person('Gosho', 11)
print(p.__dict__)
print(p.info())
#
# print(hasattr(p, 'name'))
# print(hasattr(p, 'name2'))
#
# while True:
#     attr_name = input()
#     attr = getattr(p, attr_name, -7)
#     if hasattr(attr, '__call__'):
#         print(attr())
#     else:
#         print(attr)
