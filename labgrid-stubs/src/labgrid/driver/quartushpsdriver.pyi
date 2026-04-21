from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from ..util import Timeout as Timeout
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver
from .exception import ExecutionError as ExecutionError

class QuartusHPSDriver(Driver):
    bindings: Incomplete
    image: Incomplete
    tool: Incomplete
    jtag_tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def flash(self, filename=None, address: int = 0) -> None: ...
    @Driver.check_active
    def erase(self, address=None, size=None) -> None: ...
