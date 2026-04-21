from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from ..util.managedfile import ManagedFile as ManagedFile
from .common import Driver as Driver

class BaseProviderDriver(Driver):
    @Driver.check_bound
    def get_export_vars(self): ...
    @Driver.check_active
    def stage(self, filename): ...

class TFTPProviderDriver(BaseProviderDriver):
    bindings: Incomplete

class NFSFile:
    host: Incomplete
    export: Incomplete
    relative_file_path: Incomplete

class NFSProviderDriver(Driver):
    bindings: Incomplete
    @Driver.check_bound
    def get_export_vars(self): ...
    @Driver.check_active
    def stage(self, filename): ...

class HTTPProviderDriver(BaseProviderDriver):
    bindings: Incomplete
