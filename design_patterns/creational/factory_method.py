from animals import Dog, Cat
from helpers import JsonDataExporter, StringDataExporter


# Factory method
class DataExporterFactory:
    json_exporter = None
    string_exporter = None

    def get_exporter(self, type):
        if type == 'json':
            if self.json_exporter is None:
                self.json_exporter = JsonDataExporter()
            return self.json_exporter
        else:
            return StringDataExporter()


type = 'json'  # | str
factory = DataExporterFactory()

de = factory.get_exporter(type)

animals = [
    Dog('Sharo'),
    Cat('Mima', 19),
]

[print(de.export(a)) for a in animals]
