import json
from abc import ABC, abstractmethod


class DataParser(ABC):
    @abstractmethod
    def parse(self, data: str):
        pass


# Initially, I have this
class TextParser(DataParser):
    def parse(self, text):
        """
        Doncho_19_Sofia
        """
        name, age, town = text.split('_')
        return {
            'name': name,
            'age': age,
            'town': town,
        }


# Later, this is added
# - Adapt json to my DataParser interface
class JsonParser(DataParser):
    def parse(self, data):
        return json.loads(data)


class ParsersFactory:
    def get_parser(self, data_type):
        if data_type == 'text':
            return TextParser()
        elif data_type == 'json':
            return JsonParser()


# data_type = 'text'
# data = 'Doncho_19_Burgas'
data_type = 'json'
data = '{"name":"Doncho", "age": 21, "town": "Burgas"}'

print(
    ParsersFactory()
        .get_parser(data_type)
        .parse(data)
)
