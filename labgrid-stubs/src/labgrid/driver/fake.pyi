from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import CommandProtocol as CommandProtocol
from ..protocol import ConsoleProtocol as ConsoleProtocol
from ..protocol import FileTransferProtocol as FileTransferProtocol
from ..protocol import PowerProtocol as PowerProtocol
from .commandmixin import CommandMixin as CommandMixin
from .common import Driver as Driver
from .consoleexpectmixin import ConsoleExpectMixin as ConsoleExpectMixin

class FakeConsoleDriver(ConsoleExpectMixin, Driver, ConsoleProtocol):
    txdelay: Incomplete
    txchunk: Incomplete
    rxq: Incomplete
    txq: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def open(self) -> None: ...
    def close(self) -> None: ...

class FakeCommandDriver(CommandMixin, Driver, CommandProtocol):
    @Driver.check_active
    def run(self, *args, timeout=None) -> None: ...
    @Driver.check_active
    def run_check(self, *args) -> None: ...
    @Driver.check_active
    def get_status(self) -> None: ...

class FakeFileTransferDriver(Driver, FileTransferProtocol):
    @Driver.check_active
    def get(self, *args) -> None: ...
    @Driver.check_active
    def put(self, *args) -> None: ...

class FakePowerDriver(Driver, PowerProtocol):
    @Driver.check_active
    def on(self, *args) -> None: ...
    @Driver.check_active
    def off(self, *args) -> None: ...
    @Driver.check_active
    def cycle(self, *args) -> None: ...
