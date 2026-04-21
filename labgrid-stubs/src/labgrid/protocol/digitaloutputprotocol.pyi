import abc

class DigitalOutputProtocol(abc.ABC):
    @abc.abstractmethod
    def get(self): ...
    @abc.abstractmethod
    def set(self, status): ...
