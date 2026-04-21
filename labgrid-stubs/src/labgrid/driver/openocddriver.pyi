from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import BootstrapProtocol as BootstrapProtocol
from ..step import step as step
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver

class OpenOCDDriver(Driver, BootstrapProtocol):
    bindings: Incomplete
    config: Incomplete
    search: Incomplete
    image: Incomplete
    interface_config: Incomplete
    board_config: Incomplete
    load_commands: Incomplete
    tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def load(self, filename=None) -> None: ...
    @Driver.check_active
    def execute(self, commands: list): ...
