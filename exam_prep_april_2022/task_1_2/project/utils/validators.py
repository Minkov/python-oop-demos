def validate_non_empty_string(value, err_message):
    if not isinstance(value, str) or len(value) < 1:
        raise ValueError(err_message)


def validate_greater_than_value(value, min_value, err_message):
    if value < min_value:
        raise ValueError(err_message)
