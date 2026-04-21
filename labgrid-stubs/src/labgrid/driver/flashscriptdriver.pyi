from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver

class FlashScriptDriver(Driver):
    bindings: Incomplete
    script: Incomplete
    args: Incomplete
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def flash(self, script=None, args=None) -> None: ...
