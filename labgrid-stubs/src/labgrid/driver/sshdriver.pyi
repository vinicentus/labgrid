import contextlib
from collections.abc import Generator

from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..protocol import CommandProtocol as CommandProtocol
from ..protocol import FileTransferProtocol as FileTransferProtocol
from ..step import step as step
from ..util.helper import get_free_port as get_free_port
from ..util.proxy import proxymanager as proxymanager
from ..util.ssh import get_ssh_connect_timeout as get_ssh_connect_timeout
from ..util.timeout import Timeout as Timeout
from .commandmixin import CommandMixin as CommandMixin
from .common import Driver as Driver
from .exception import ExecutionError as ExecutionError

class SSHDriver(CommandMixin, Driver, CommandProtocol, FileTransferProtocol):
    bindings: Incomplete
    priorities: Incomplete
    keyfile: Incomplete
    stderr_merge: Incomplete
    connection_timeout: Incomplete
    explicit_sftp_mode: Incomplete
    explicit_scp_mode: Incomplete
    username: Incomplete
    password: Incomplete
    def __attrs_post_init__(self) -> None: ...
    ssh_prefix: Incomplete
    control: Incomplete
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @property
    def skip_deactivate_on_export(self): ...
    @Driver.check_active
    def run(self, cmd, codec: str = "utf-8", decodeerrors: str = "strict", timeout=None): ...
    def interact(self, cmd=None): ...
    @Driver.check_active
    @contextlib.contextmanager
    def forward_local_port(self, remoteport, localport=None) -> Generator[Incomplete]: ...
    @Driver.check_active
    @contextlib.contextmanager
    def forward_remote_port(self, remoteport, localport) -> Generator[None]: ...
    @Driver.check_active
    @contextlib.contextmanager
    def forward_unix_socket(self, unixsocket, localport=None) -> Generator[Incomplete]: ...
    @Driver.check_active
    def scp(self, *, src, dst): ...
    @Driver.check_active
    def rsync(self, *, src, dst, extra=[]): ...
    @Driver.check_active
    def sshfs(self, *, path, mountpoint) -> None: ...
    def get_status(self): ...
    @Driver.check_active
    def put(self, filename, remotepath: str = "") -> None: ...
    @Driver.check_active
    def get(self, filename, destination: str = ".") -> None: ...
