from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import VideoProtocol as VideoProtocol
from ..util.proxy import proxymanager as proxymanager
from .common import Driver as Driver

class HTTPVideoDriver(Driver, VideoProtocol):
    bindings: Incomplete
    def get_qualities(self): ...
    @Driver.check_active
    def stream(self, quality_hint=None): ...
