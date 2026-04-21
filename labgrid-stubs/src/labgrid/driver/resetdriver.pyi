from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import DigitalOutputProtocol as DigitalOutputProtocol
from ..protocol import ResetProtocol as ResetProtocol
from ..step import step as step
from .common import Driver as Driver

class DigitalOutputResetDriver(Driver, ResetProtocol):
    bindings: Incomplete
    delay: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def reset(self) -> None: ...
