class DataProcessor:
    def process(self, data_list):
        if not data_list:
            return None
        dd = {}
        for value in data_list:
            if value not in dd:
                dd[value] = 0
            dd[value] += 1

        return dd


class RemainderDataProcessor(DataProcessor):
    def __init__(self, divisor):
        self.divisor = divisor

    # Violation of LSP - different behavior
    def process(self, data_list):
        dd = {}
        for value in data_list:
            remainder = value % self.divisor
            if remainder not in dd:
                dd[remainder] = 0
            dd[remainder] += 1

        return dd


class RemainderDataProcessor2(DataProcessor):
    def __init__(self, divisor):
        self.divisor = divisor

    # Violation of LSP - different behavior
    def process(self, data_list):
        dd = {}
        for value in data_list:
            remainder = value % self.divisor
            if remainder not in dd:
                dd[remainder] = []
            dd[remainder].append(value)

        return dd


# print(DataProcessor().process([]))
# print(DataProcessor().process(None))
# print(DataProcessor().process([1, 2, 3, 2]))
#
# print(RemainderDataProcessor(2).process([]))
# print(RemainderDataProcessor(2).process(None))
# print(RemainderDataProcessor(2).process([1, 2, 3, 2]))

# result = DataProcessor().process([])
result = RemainderDataProcessor(2).process([])
if result is None:
    print('No elements')
else:
    print(result)
