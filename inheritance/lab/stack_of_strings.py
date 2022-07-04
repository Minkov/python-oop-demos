class StringStack:
    def __init__(self):
        self.data = []

    def validate_if_string(self, value):
        if not isinstance(value, str):
            raise TypeError('Only strings can be appended to StringStack')

    def push(self, value):
        self.validate_if_string(value)
        self.data.append(value)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return str(self.data)
