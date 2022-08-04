import abc


class MyClass(abc.ABC):
    pass


class MyClass2:
    @abc.abstractmethod
    def d2(self):
        pass


class MyClass3(abc.ABC):
    @abc.abstractmethod
    def d2(self):
        pass


print(MyClass())
print(MyClass2())
print(MyClass3())
