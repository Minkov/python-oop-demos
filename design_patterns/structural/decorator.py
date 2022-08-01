from animals import Cat
from helpers.exporters import DataExporter, JsonDataExporter


class EncryptDataExporter(DataExporter):
    def __init__(self, exporter):
        self.exporter = exporter

    @staticmethod
    def __encrypt(value):
        return f'--{value}--'

    def export(self, data):
        for key in data.__dict__.keys():
            value = getattr(data, key)
            encrypted_value = self.__encrypt(value)
            setattr(data, key, encrypted_value)
        return self.exporter.export(data)


exporter = EncryptDataExporter(JsonDataExporter())
cat = Cat('Mima', 19)
print(exporter.export(cat))
print(cat.name)
