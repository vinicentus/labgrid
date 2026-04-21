from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import DigitalOutputProtocol as DigitalOutputProtocol
from ..step import step as step
from .common import Driver as Driver

class FileDigitalOutputDriver(Driver, DigitalOutputProtocol):
    filepath: Incomplete
    false_repr: Incomplete
    true_repr: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def get(self): ...
    @Driver.check_active
    def set(self, status) -> None: ...
