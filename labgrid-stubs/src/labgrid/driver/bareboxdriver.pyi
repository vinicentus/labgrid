from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import CommandProtocol as CommandProtocol
from ..protocol import ConsoleProtocol as ConsoleProtocol
from ..protocol import LinuxBootProtocol as LinuxBootProtocol
from ..step import step as step
from ..util import Timeout as Timeout
from ..util import gen_marker as gen_marker
from ..util import re_vt100 as re_vt100
from .commandmixin import CommandMixin as CommandMixin
from .common import Driver as Driver

class BareboxDriver(CommandMixin, Driver, CommandProtocol, LinuxBootProtocol):
    bindings: Incomplete
    prompt: Incomplete
    autoboot: Incomplete
    interrupt: Incomplete
    bootstring: Incomplete
    password: Incomplete
    boot_command: Incomplete
    login_timeout: Incomplete
    saved_log_level: int
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def run(self, cmd: str, *, timeout: int = 30): ...
    @Driver.check_active
    def reset(self) -> None: ...
    def get_status(self): ...
    @Driver.check_active
    def await_boot(self) -> None: ...
    @Driver.check_active
    def boot(self, name: str = ""): ...
