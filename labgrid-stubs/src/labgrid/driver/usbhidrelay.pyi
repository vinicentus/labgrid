from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import DigitalOutputProtocol as DigitalOutputProtocol
from ..resource.remote import NetworkHIDRelay as NetworkHIDRelay
from ..step import step as step
from ..util.agentwrapper import AgentWrapper as AgentWrapper
from .common import Driver as Driver

class HIDRelayDriver(Driver, DigitalOutputProtocol):
    bindings: Incomplete
    wrapper: Incomplete
    def __attrs_post_init__(self) -> None: ...
    proxy: Incomplete
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def set(self, status) -> None: ...
    @Driver.check_active
    def get(self): ...
