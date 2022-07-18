class NumbersValidator:
    min_value = 0
    max_value = 1024

    def validate(self, value):
        if value < self.min_value or self.max_value < value:
            raise ValueError(f'Value is outside the range [{self.min_value}, {self.max_value}]')


class NegativeNumbersValidator(NumbersValidator):
    min_value = -1024
    max_value = 0

    def validate(self, value):
        # Violation of LSP
        if value < self.min_value or self.max_value < value:
            return False
        return True
        # return value < self.min_value or self.max_value < value:


validators = [
    NumbersValidator(),
    NegativeNumbersValidator(),
]

numbers = [1, -1]
for validator in validators:
    for number in numbers:
        try:
            validator.validate(number)
            print(f'{number} is valid')
        except:
            print(f'{number} is invalid')
