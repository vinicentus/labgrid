import abc

class VideoProtocol(abc.ABC):
    @abc.abstractmethod
    def get_qualities(self): ...
    @abc.abstractmethod
    def stream(self, quality_hint=None): ...
