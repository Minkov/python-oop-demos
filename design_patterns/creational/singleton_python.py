def singleton(cls):
    cls.instance = None

    def wrapper(*args, **kwargs):
        if cls.instance is None:
            cls.instance = cls(*args, **kwargs)
        return cls.instance

    return wrapper


@singleton
class MyClass:
    pass


mc1 = MyClass()
mc2 = MyClass()
print(mc1 == mc2)
print(mc1)
print(mc2)
