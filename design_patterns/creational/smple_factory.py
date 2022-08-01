
from animals import Dog, Cat


# Simple factory
from helpers import JsonDataExporter, StringDataExporter


def create_data_exporter(type):
    if type == 'json':
        return JsonDataExporter()
    else:
        return StringDataExporter()


type = 'json'  # | str

de = create_data_exporter(type)
animals = [
    Dog('Sharo'),
    Cat('Mima', 19),
]

[print(de.export(a)) for a in animals]
