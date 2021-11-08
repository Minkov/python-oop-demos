class ValidationResult:
    def __init__(self, is_success, error_message=None):
        self.is_success = is_success
        self.error_message = error_message

    @classmethod
    def success(cls):
        return cls(True)

    @classmethod
    def error(cls, error_message):
        return cls(False, error_message)


print(ValidationResult(True).__dict__)
print(ValidationResult(False, "Some error").__dict__)

print(ValidationResult.success().__dict__)
print(ValidationResult.error('Another error').__dict__)


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ['bread'] + ingredients

    @classmethod
    def pepperoni(cls):
        return cls(['tomato sauce', 'parmesan', 'pepperoni'])


class ItalianPizza(Pizza):
    def __init__(self, ingredients):
        super().__init__(ingredients)
        self.ingredients = ['italian bread'] + ingredients


print(Pizza.pepperoni().__dict__)
print(Pizza(['tomato sauce', 'parmesan', 'pepperoni']).__dict__)

print(ItalianPizza.pepperoni().__dict__)
