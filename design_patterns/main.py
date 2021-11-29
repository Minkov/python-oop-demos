# junior developer

print('Hello world')


# mid-level developer

class HelloWorldPrinter:
    def __init__(self, message):
        self.message = message

    def print(self):
        print(self.message)


HelloWorldPrinter('Hello, world!').print()


# senior developer

class HelloWorldPrinterFactory:
    @staticmethod
    def get_printer(message):
        return HelloWorldPrinter(message)


HelloWorldPrinterFactory.get_printer('Hello, world!').print()

# architect
# over-architecture, overdesign, ....

print('Hello, world!')

# gof - gang of four
