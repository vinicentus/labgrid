from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import PowerProtocol as PowerProtocol
from ..resource.remote import NetworkSigrokUSBDevice as NetworkSigrokUSBDevice
from ..resource.remote import NetworkSigrokUSBSerialDevice as NetworkSigrokUSBSerialDevice
from ..resource.sigrok import SigrokDevice as SigrokDevice
from ..resource.udev import SigrokUSBDevice as SigrokUSBDevice
from ..resource.udev import SigrokUSBSerialDevice as SigrokUSBSerialDevice
from ..step import step as step
from ..util import Timeout as Timeout
from ..util.helper import processwrapper as processwrapper
from .common import Driver as Driver
from .common import check_file as check_file
from .exception import ExecutionError as ExecutionError
from .powerdriver import PowerResetMixin as PowerResetMixin

class SigrokCommon(Driver):
    tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...

class SigrokDriver(SigrokCommon):
    bindings: Incomplete
    @Driver.check_active
    def capture(self, filename, samplerate: str = "200k") -> None: ...
    @Driver.check_active
    def stop(self): ...
    @Driver.check_active
    def analyze(self, args, filename=None): ...

class SigrokPowerDriver(SigrokCommon, PowerResetMixin, PowerProtocol):
    bindings: Incomplete
    delay: Incomplete
    max_voltage: Incomplete
    max_current: Incomplete
    @Driver.check_active
    def on(self) -> None: ...
    @Driver.check_active
    def off(self) -> None: ...
    @Driver.check_active
    def cycle(self) -> None: ...
    @Driver.check_active
    def set_voltage_target(self, value) -> None: ...
    @Driver.check_active
    def set_current_limit(self, value) -> None: ...
    @Driver.check_active
    def get(self): ...
    @Driver.check_active
    def measure(self): ...

class SigrokDmmDriver(SigrokCommon):
    bindings: Incomplete
    @Driver.check_active
    def capture(self, samples, timeout=None) -> None: ...
    @Driver.check_active
    def stop(self): ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
