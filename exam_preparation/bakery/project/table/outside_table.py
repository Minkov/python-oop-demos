from project.table.table import Table


class OutsideTable(Table):
    _MIN_TABLE_NUMBER = 51
    _MAX_TABLE_NUMBER = 100
    _INVALID_TABLE_NUMBER_MESSAGE = 'Outside table\'s number must be between 51 and 100 inclusive!'

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

    @property
    def table_type(self):
        return 'OutsideTable'
