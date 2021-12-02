from project.table.table import Table


class InsideTable(Table):
    _MIN_TABLE_NUMBER = 1
    _MAX_TABLE_NUMBER = 50
    _INVALID_TABLE_NUMBER_MESSAGE = 'Inside table\'s number must be between 1 and 50 inclusive!'

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_type(self):
        return 'InsideTable'