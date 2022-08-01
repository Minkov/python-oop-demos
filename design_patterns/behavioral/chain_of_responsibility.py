import abc


class Handler(abc.ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def _handle(self, value):
        pass

    @abc.abstractmethod
    def _can_handle(self, value) -> bool:
    pass

    def handle(self, value):
        if not self._can_handle(value):
            return self.next_handler.handle(value)
        return self._handle(value)


class IntsHandler(Handler):
    def _can_handle(self, value):
        return isinstance(value, int)

    def _handle(self, value):
        return f'{value} is int'


class IntsDividableByBaseHandler(IntsHandler):
    def __init__(self, base, next_handler=None):
        super().__init__(next_handler)
        self.base = base

    def _can_handle(self, value) -> bool:
        return super()._can_handle(value) \
               and value % self.base == 0

    def _handle(self, value):
        return super()._handle(value) + f' dividable by {self.base}'


class FloatsHandler(Handler):
    def _can_handle(self, value):
        return isinstance(value, float)

    def _handle(self, value):
        return f'{value} is float'


class AllHandler(Handler):
    def _can_handle(self, value) -> bool:
        return True

    def _handle(self, value):
        return f'{value} is of unknown type'


def build_handlers(handlers):
    for i in range(1, len(handlers)):
        handlers[i - 1].next_handler = handlers[i]
    return handlers[0]


handlers = [
    IntsDividableByBaseHandler(3),
    IntsHandler(),
    FloatsHandler(),
    AllHandler(),
]
root_handler = build_handlers(handlers)

values = [
    3,
    1,
    1.3,
    'str',
    None,
    {},
    {1},
    [1, 2, 3, ]
]

[print(root_handler.handle(value)) for value in values]
