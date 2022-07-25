def uppercase(func):  # The **Decorator**
    def wrapper():
        result = func()
        return result.upper()

    return wrapper