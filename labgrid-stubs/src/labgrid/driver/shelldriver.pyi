from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import CommandProtocol as CommandProtocol
from ..protocol import ConsoleProtocol as ConsoleProtocol
from ..protocol import FileTransferProtocol as FileTransferProtocol
from ..step import step as step
from ..util import Timeout as Timeout
from ..util import gen_marker as gen_marker
from ..util import re_vt100 as re_vt100
from .commandmixin import CommandMixin as CommandMixin
from .common import Driver as Driver
from .exception import ExecutionError as ExecutionError

class ShellDriver(CommandMixin, Driver, CommandProtocol, FileTransferProtocol):
    bindings: Incomplete
    prompt: Incomplete
    login_prompt: Incomplete
    username: Incomplete
    password: Incomplete
    keyfile: Incomplete
    login_timeout: Incomplete
    console_ready: Incomplete
    await_login_timeout: Incomplete
    post_login_settle_time: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def run(self, cmd, timeout: float = 30.0, codec: str = "utf-8", decodeerrors: str = "strict"): ...
    def get_status(self): ...
    @Driver.check_active
    def put_ssh_key(self, keyfile_path) -> None: ...
    @Driver.check_active
    def put_bytes(self, buf: bytes, remotefile: str): ...
    @Driver.check_active
    def put(self, localfile: str, remotefile: str): ...
    @Driver.check_active
    def get_bytes(self, remotefile: str): ...
    @Driver.check_active
    def get(self, remotefile: str, localfile: str): ...
    @Driver.check_active
    def run_script(self, data: bytes, timeout: int = 60): ...
    @Driver.check_active
    def run_script_file(self, scriptfile: str, *args, timeout: int = 60): ...
    @Driver.check_active
    def get_default_interface_device_name(self, version: int = 4): ...
    @Driver.check_active
    def get_ip_addresses(self, device=None): ...
