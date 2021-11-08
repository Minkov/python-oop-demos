class Person:
    _min_name_length = 2
    _max_name_length = 15
    _valid_name_characters = 'qwertyuiopasdfghjklzxcvbnm'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self.__name = value

    @classmethod
    def _validate_name_length(cls, value):
        value_len = len(value)
        if value_len < cls._min_name_length \
                or cls._max_name_length < value_len:
            raise ValueError(f'The length of the name must between {cls._min_name_length}'
                             f' and {cls._max_name_length}')

    @classmethod
    def _validate_name_characters(cls, value):
        has_invalid_characters = any(x.lower() not in cls._valid_name_characters for x in value)
        if has_invalid_characters:
            raise ValueError(f'Name must contain only the following characters: {cls._valid_name_characters}')

    @classmethod
    def _validate_name(cls, value):
        cls._validate_name_length(value)
        cls._validate_name_characters(value)


class Teacher(Person):
    _min_name_length = 4

    @classmethod
    def _validate_name_characters(cls, value):
        if not value.lower().startswith('mr. ') \
                and not value.lower().startswith('ms.'):
            raise ValueError('Teacher name must start with either "Ms." or "Mr."')
        Person._validate_name_characters(value[4:])


# st = Teacher('Mr. Doncho', 19)
print(Teacher('Mr. Doncho', 19).__dict__)
print(Teacher('Ms. Tigar', 19).__dict__)
print(Teacher('Doncho', 19).__dict__)

'''
static -> independent from class state & class behavior
class -> independent from instance state & instance behavior
instance -> instance state, behavior + super()
'''

'''
instead of `class`, use:
1. cls
2. klass
3. clazz
4. clas
5. klazz
6. kl
'''
