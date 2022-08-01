import abc
import json


class DataExporter(abc.ABC):
    @abc.abstractmethod
    def export(self, data):
        pass


# Adapter
class JsonDataExporter(DataExporter):
    def export(self, data):
        return json.dumps(data.__dict__)


# Adapter
class StringDataExporter(DataExporter):
    def export(self, data):
        return str(data)
