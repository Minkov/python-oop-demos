from decorators.log import log


@log(filepath='./logs.txt')
def say_hello(name):
    print(f'Hello, {name}! How are you?')


@log
def say_hi():
    print('Hi!')


say_hello('Doncho')
say_hi()
print('Test')
