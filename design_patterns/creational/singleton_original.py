class MyClass:
    __instance = None

    def __init__(self):
        if self.__instance is not None:
            raise TypeError('Singleton\'s cannot be created with init')

    @classmethod
    @property
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = MyClass()
        return cls.__instance


mc1 = MyClass.instance
mc2 = MyClass.instance
print(mc1 == mc2)
print(mc1)
print(mc2)
MyClass()
