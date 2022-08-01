import abc
import os
import uuid


class UiComponent(abc.ABC):
    def __init__(self, identifier):
        self.identifier = identifier

    # `__repr__` is this exact example
    @abc.abstractmethod
    def get_representation(self):
        pass

    def __str__(self):
        return self.get_representation()


class Heading(UiComponent):
    def __init__(self, identifier, text):
        super().__init__(identifier)
        self.text = text

    def get_representation(self):
        return f'*{self.text}*'


class Button(UiComponent):
    def __init__(self, identifier, text, func):
        super().__init__(identifier)
        self.text = text
        self.func = func

    def click(self, *args, **kwargs, ):
        return self.func(self, *args, **kwargs)

    def get_representation(self):
        return f'[{self.text}]'


class Text(UiComponent):
    def __init__(self, identifier, text):
        super().__init__(identifier)
        self.text = text

    def get_representation(self):
        return f'{self.text}'


# Composite
class UiComponentsComposition(UiComponent):
    def __init__(self, identifier, children=None):
        super().__init__(identifier)
        if children is None:
            children = []
        self.children = children


# Composite
class Container(UiComponentsComposition):
    def get_representation(self):
        return ''.join(c.get_representation() for c in self.children)


# Composite
class VerticalList(UiComponentsComposition):
    def get_representation(self):
        return os.linesep.join(f' - {c.get_representation()}' for c in self.children)


class NewLine(UiComponent):
    def __init__(self):
        super().__init__(uuid.uuid4())

    def get_representation(self):
        return os.linesep


print(Heading('heading-1', 'It works!'))

print(
    Container(
        'container-1',
        [
            Heading('h1', 'It works'),
            Button('btn-1', 'Click me', None),
            NewLine(),
            VerticalList(
                'list-1',
                [
                    Heading('h2', 'It works, again'),
                    Button('btn-2', 'Don\'t click me', None),
                    Text('txt-1', 'I am text'),
                ]
            )
        ]
    )
)
