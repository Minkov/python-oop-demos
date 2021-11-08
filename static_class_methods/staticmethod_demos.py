def create_id_generator():
    x = 0

    def get_id():
        nonlocal x
        x += 1
        return x

    return get_id


def validate_age(age):
    if age < 0:
        raise ValueError('Age cannot be negative')


def validate_name(name):
    pass


class Person:
    _min_name_length = 2
    _max_name_length = 15
    get_id = create_id_generator()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Person.get_id()

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, value):
        self.validate_name(value)
        self.__name = value

    @age.setter
    def age(self, value):
        validate_age(value)
        self.__age = value

    @staticmethod
    def validate_name(value):
        if len(value) < 2 \
                or 15 < len(value):
            raise ValueError(
                f'Name must be between 2 and 15 characters long!')

    def is_age_valid(self, age):
        try:
            validate_age(age)
            return True
        except:
            return False


def validate_student_age(age):
    if age < 7:
        raise ValueError('Students must be at least 7-years-old!')


class Student(Person):
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        validate_student_age(value)
        self.__age = value

    def is_age_valid(self, age):
        try:
            validate_student_age(age)
            return True
        except:
            return False

    @staticmethod
    def validate_name(value):
        # super().validate_name(value) for instance methods
        Person.validate_name(value)
        if len(value) < 5:
            raise ValueError('Name must be at least 5-characters-long')


# Person('au', 12)
# st = Student('asdasd', 8)
# print(f'Is 3 a valid age?: {st.is_age_valid(3)}')
# # Student('aqweu', 5)
#
# print(st.is_age_valid(6), False)
# print(st.is_age_valid(7), True)

for i in range(5):
    print(Person('asd', 5).__dict__)
