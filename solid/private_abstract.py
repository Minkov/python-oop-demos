import abc


# Private abstract methods are impossible
class Base(abc.ABC):
    @abc.abstractmethod
    def __m(self):
        pass

    def print(self):
        print(self.__m())


class Derived(Base):
    def __m(self):
        return 'It works'


Derived().print()
