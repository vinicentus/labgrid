from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..resource import NetworkDediprogFlasher as NetworkDediprogFlasher
from ..step import step as step
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver
from .common import check_file as check_file

class DediprogFlashDriver(Driver):
    bindings: Incomplete
    image: Incomplete
    tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    def map_vcc(self): ...
    @Driver.check_active
    def __call__(self, *args) -> None: ...
    @Driver.check_active
    def flash(self, filename=None) -> None: ...
    @Driver.check_active
    def erase(self) -> None: ...
