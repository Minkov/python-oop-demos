class PostgreSQL:
    pass


class StudentsController:
    def __init__(self):
        self.db = PostgreSQL()


class StudentsController2:
    def __init__(self, db):
        self.db = db


# Production:

sc = StudentsController()  # works with PostgreSQL
sc2 = StudentsController2(PostgreSQL())  # works with PostgreSQL


# Testing:

class FakeDb:
    '''
    Saves data in a list
    '''
    pass


sc = StudentsController()  # works with PostgreSQL
sc2 = StudentsController2(FakeDb())  # works with lists
