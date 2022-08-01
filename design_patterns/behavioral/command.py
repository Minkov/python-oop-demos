import abc
import sys
from io import StringIO


class Command(abc.ABC):
    @abc.abstractmethod
    def execute(self, *args, **kwargs):
        pass


class AddCommand(Command):
    def __init__(self, values, value):
        self.values = values
        self.value = value

    def execute(self, *args, **kwargs):
        self.values.append(self.value)


class SumCommand(Command):
    def __init__(self, values):
        self.values = values

    def execute(self, *args, **kwargs):
        return sum(self.values)


class ListCommand(Command):
    def __init__(self, values):
        self.values = values

    def execute(self, *args, **kwargs):
        return self.values


class GenericCommand(Command):
    def __init__(self, func):
        self.func = func

    def execute(self, *args, **kwargs):
        return self.func(*args, **kwargs)


sys.stdin = StringIO(
    '''Add 1
Add 2
Sum
List
Add 4
Sum
List
End
'''
)

ll = []
commands = []
while True:
    command = input()
    if command == 'End':
        break

    # Can be moved to a factory
    if command.startswith('Add'):
        _, value_str = command.split(' ')
        commands.append(AddCommand(ll, int(value_str)))
    elif command == 'List':
        commands.append(ListCommand(ll))
    elif command == 'Sum':
        commands.append(SumCommand(ll))
#
# while True:
#     command = input()
#     if command == 'End':
#         break
#
#     # Can be moved to a factory
#     if command.startswith('Add'):
#         _, value_str = command.split(' ')
#         value = int(value_str)
#         # commands.append(GenericCommand(lambda: ll.append(value)))
#         # commands.append(lambda: ll.append(value)) # funcs are first-class citizens
#     elif command == 'List':
#         commands.append(GenericCommand(lambda: ll))
#     elif command == 'Sum':
#         commands.append(GenericCommand(lambda: sum(ll)))

print(ll)
for command in commands:
    result = command.execute()
    if result:
        print(result)
