import abc

from helpers import JsonDataExporter


class DataExporterFactory(abc.ABC):
    @abc.abstractmethod
    def create_exporter(self):
        pass


class JsonExporterFactory(DataExporterFactory):
    exporter = None

    def create_exporter(self):
        if self.exporter is None:
            self.exporter = JsonDataExporter()
        return self.exporter


class DataExporterFactoryFactory:
    pass


type = 'json'
