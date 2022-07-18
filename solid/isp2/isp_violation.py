class Validator:
    def validate_in_range(self, value, min_value, max_value):
        if value < min_value or max_value < value:
            raise ValueError()

    def validate_greater_than(self, value, min_value):
        if value <= min_value:
            raise ValueError()


validator = Validator()
validator.validate_in_range(3, 3, 5)
validator.validate_in_range(4, 3, 5)
validator.validate_greater_than(4, 3)
validator.validate_greater_than(4, 4)
