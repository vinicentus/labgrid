from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import DigitalOutputProtocol as DigitalOutputProtocol
from ..util.proxy import proxymanager as proxymanager
from .common import Driver as Driver
from .exception import ExecutionError as ExecutionError

class ModbusCoilDriver(Driver, DigitalOutputProtocol):
    bindings: Incomplete
    client: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def set(self, status) -> None: ...
    @Driver.check_active
    def get(self): ...

class WaveShareModbusCoilDriver(ModbusCoilDriver):
    bindings: Incomplete
    @Driver.check_active
    def get(self): ...
    def __attrs_post_init__(self) -> None: ...
