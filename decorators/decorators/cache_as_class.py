class cache:
    def __init__(self, func):
        """
        same as `decorator` func
        :param func:
        """
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        """
        same as `wrapper` func
        """

        self.__ensure_value_in_cache(*args, **kwargs)
        key = self.__build_key(*args, **kwargs)
        return self.cache[key]

    def __ensure_value_in_cache(self, *args, **kwargs):
        key = self.__build_key(*args, **kwargs)
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)

    @staticmethod
    def __build_key(*args, **kwargs):
        return args + tuple(kwargs.items())
