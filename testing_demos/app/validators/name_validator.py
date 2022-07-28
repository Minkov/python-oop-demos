class ValidationException(Exception):
    pass


MIN_NAME_LENGTH = 2
MAX_NAME_LENGTH = 30


def validate_name(name):
    if name is None:
        raise ValidationException('Name cannot be `None`')

    if not isinstance(name, str):
        raise ValidationException('Name must be a `string`')

    name_len = len(name)

    if name_len < MIN_NAME_LENGTH or MAX_NAME_LENGTH < name_len:
        raise ValidationException(f'Name must be between {MIN_NAME_LENGTH} and {MAX_NAME_LENGTH} characters long')
