from _typeshed import Incomplete

from ..exceptions import InvalidConfigError as InvalidConfigError
from ..factory import target_factory as target_factory
from ..resource.fastboot import AndroidNetFastboot as AndroidNetFastboot
from ..resource.remote import RemoteAndroidNetFastboot as RemoteAndroidNetFastboot
from ..resource.remote import RemoteAndroidUSBFastboot as RemoteAndroidUSBFastboot
from ..resource.udev import AndroidUSBFastboot as AndroidUSBFastboot
from ..step import step as step
from ..util.helper import processwrapper as processwrapper
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver

class AndroidFastbootDriver(Driver):
    bindings: Incomplete
    boot_image: Incomplete
    flash_images: Incomplete
    sparse_size: Incomplete
    tool: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    @Driver.check_active
    def __call__(self, *args) -> None: ...
    @Driver.check_active
    def boot(self, filename=None) -> None: ...
    @Driver.check_active
    def flash(self, partition, filename=None) -> None: ...
    @Driver.check_active
    def flash_all(self) -> None: ...
    @Driver.check_active
    def erase(self, partition) -> None: ...
    @Driver.check_active
    def run(self, cmd) -> None: ...
    @Driver.check_active
    def continue_boot(self) -> None: ...
    @Driver.check_active
    def getvar(self, var): ...
    @Driver.check_active
    def oem_getenv(self, var): ...
