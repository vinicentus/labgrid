from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import ConsoleProtocol as ConsoleProtocol
from ..protocol import PowerProtocol as PowerProtocol
from ..step import step as step
from ..util.qmp import QMPError as QMPError
from ..util.qmp import QMPMonitor as QMPMonitor
from .common import Driver as Driver
from .consoleexpectmixin import ConsoleExpectMixin as ConsoleExpectMixin
from .exception import ExecutionError as ExecutionError

class QEMUDriver(ConsoleExpectMixin, Driver, PowerProtocol, ConsoleProtocol):
    qemu_bin: Incomplete
    machine: Incomplete
    cpu: Incomplete
    memory: Incomplete
    extra_args: Incomplete
    boot_args: Incomplete
    kernel: Incomplete
    disk: Incomplete
    disk_opts: Incomplete
    rootfs: Incomplete
    dtb: Incomplete
    flash: Incomplete
    bios: Incomplete
    display: Incomplete
    nic: Incomplete
    status: int
    txdelay: Incomplete
    txchunk: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def get_qemu_version(self, qemu_bin): ...
    def get_qemu_base_args(self): ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    qmp: Incomplete
    def on(self) -> None: ...
    def off(self) -> None: ...
    def cycle(self) -> None: ...
    def monitor_command(self, command, arguments={}): ...
    def add_port_forward(
        self,
        proto,
        local_address,
        local_port,
        remote_address,
        remote_port,
        netdev: str = "",
    ) -> None: ...
    def remove_port_forward(self, proto, local_address, local_port, netdev: str = "") -> None: ...
