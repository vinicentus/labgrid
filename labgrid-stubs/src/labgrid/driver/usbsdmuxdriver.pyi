from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from ..util.helper import processwrapper as processwrapper
from .common import Driver as Driver
from .exception import ExecutionError as ExecutionError

class USBSDMuxDriver(Driver):
    bindings: Incomplete
    tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def set_mode(self, mode) -> None: ...
    @Driver.check_active
    def get_mode(self): ...
