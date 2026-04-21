from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import BootstrapProtocol as BootstrapProtocol
from ..resource import NetworkFlashrom as NetworkFlashrom
from ..step import step as step
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver
from .common import check_file as check_file

class FlashromDriver(Driver, BootstrapProtocol):
    bindings: Incomplete
    image: Incomplete
    tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def __call__(self, *args) -> None: ...
    @Driver.check_active
    def load(self, filename=None) -> None: ...
