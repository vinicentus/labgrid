from _typeshed import Incomplete

from ..driver.exception import ExecutionError as ExecutionError
from ..resource.common import NetworkResource as NetworkResource
from ..resource.common import Resource as Resource
from .helper import get_user as get_user
from .ssh import sshmanager as sshmanager

class ManagedFileError(Exception): ...

class ManagedFile:
    local_path: Incomplete
    resource: Incomplete
    detect_nfs: Incomplete
    logger: Incomplete
    hash: Incomplete
    rpath: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def sync_to_resource(self, symlink=None) -> None: ...
    def get_remote_path(self): ...
    def get_hash(self): ...
    def get_user_cache_path(self): ...
