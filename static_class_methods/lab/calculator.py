class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        r = 1
        for x in args:
            r *= x

        return r

    @staticmethod
    def divide(initial, *args):
        r = initial
        for x in args:
            r /= x

        return r

    @staticmethod
    def subtract(initial, *args):
        r = initial
        for x in args:
            r -= x

        return r


print(Calculator.add(5, 10, 4))  # 19
print(Calculator.multiply(1, 2, 3, 5))  # 30
print(Calculator.divide(100, 2))  # 50.0
#  100 /  2, 1 / 100 / 2
print(Calculator.subtract(90, 20, -50, 43, 7))  # 70

'''
90 - 20 -(-50) - 43  - 7
90  - 20 
'''
