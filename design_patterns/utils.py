class StrDictMixin:
    def __str__(self):
        return '; '.join(
            f'{key}={value}' for key, value in self.__dict__.items()
        )
