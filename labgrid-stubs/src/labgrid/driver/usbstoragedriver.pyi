import enum

from _typeshed import Incomplete

from ..driver.exception import ExecutionError as ExecutionError
from ..factory import target_factory as target_factory
from ..resource.remote import RemoteUSBResource as RemoteUSBResource
from ..step import step as step
from ..util import Timeout as Timeout
from ..util.agentwrapper import AgentWrapper as AgentWrapper
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver

class Mode(enum.Enum):
    DD = "dd"
    BMAPTOOL = "bmaptool"

class USBStorageDriver(Driver):
    bindings: Incomplete
    image: Incomplete
    WAIT_FOR_MEDIUM_TIMEOUT: float
    WAIT_FOR_MEDIUM_SLEEP: float
    MOUNT_RETRIES: int
    wrapper: Incomplete
    proxy: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    devpath: Incomplete
    @Driver.check_active
    def write_files(self, sources, target, partition, target_is_directory: bool = True) -> None: ...
    @Driver.check_active
    def write_image(self, filename=None, mode=..., partition=None, skip: int = 0, seek: int = 0) -> None: ...
    @Driver.check_active
    def get_size(self, partition=None): ...
