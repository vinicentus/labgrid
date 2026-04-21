import abc

class FileSystemProtocol(abc.ABC):
    @abc.abstractmethod
    def read(self, filename: str): ...
    @abc.abstractmethod
    def write(self, filename: str, data: bytes, append: bool): ...
