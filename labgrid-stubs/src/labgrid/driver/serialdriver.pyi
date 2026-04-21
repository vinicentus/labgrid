from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import ConsoleProtocol as ConsoleProtocol
from ..resource import SerialPort as SerialPort
from ..util.proxy import proxymanager as proxymanager
from .common import Driver as Driver
from .consoleexpectmixin import ConsoleExpectMixin as ConsoleExpectMixin

class SerialDriver(ConsoleExpectMixin, Driver, ConsoleProtocol):
    bindings: Incomplete
    txdelay: Incomplete
    txchunk: Incomplete
    timeout: Incomplete
    serial: Incomplete
    status: int
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_bound
    def get_export_vars(self): ...
    def open(self) -> None: ...
    def close(self) -> None: ...
