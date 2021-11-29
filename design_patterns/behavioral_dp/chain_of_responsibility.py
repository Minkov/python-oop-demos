from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    @abstractmethod
    def can_handle(self, *args):
        pass

    @abstractmethod
    def handle(self, *args):
        pass

    def run(self, *args):
        if not self.can_handle(*args):
            return self.next_handler.run(*args)
        return self.handle(*args)


class IntsHandler(Handler):
    def can_handle(self, *args):
        return args and isinstance(args[0], int)

    def handle(self, *args):
        print(f'The integer {args[0]}')


class StrHandler(Handler):
    def can_handle(self, *args):
        return args and isinstance(args[0], str)

    def handle(self, *args):
        print(f'The string {args[0]}')


class NoneHandler(Handler):
    def can_handle(self, *args):
        return not args or args[0] is None

    def handle(self, *args):
        print(f'This is None')


class MainHandler:
    def __init__(self):
        self.handlers = []

    def register(self, handler):
        if self.handlers:
            self.handlers[-1].next_handler = handler
        self.handlers.append(handler)

    def run(self, *args):
        return self.handlers[0].run(*args)


mh = MainHandler()
mh.register(IntsHandler())
mh.register(StrHandler())
mh.register(NoneHandler())

mh.run(5)
mh.run('5')
mh.run(None)
mh.run([None])
