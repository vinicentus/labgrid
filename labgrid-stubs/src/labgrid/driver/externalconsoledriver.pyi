from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import ConsoleProtocol as ConsoleProtocol
from .common import Driver as Driver
from .consoleexpectmixin import ConsoleExpectMixin as ConsoleExpectMixin
from .exception import ExecutionError as ExecutionError

class ExternalConsoleDriver(ConsoleExpectMixin, Driver, ConsoleProtocol):
    cmd: Incomplete
    txdelay: Incomplete
    txchunk: Incomplete
    status: int
    def __attrs_post_init__(self) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
