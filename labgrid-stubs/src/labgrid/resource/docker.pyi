from _typeshed import Incomplete

from labgrid.util.dict import find_dict as find_dict

from ..factory import target_factory as target_factory
from .common import ManagedResource as ManagedResource
from .common import ResourceManager as ResourceManager

class DockerConstants:
    DOCKER_LG_CLEANUP_LABEL: str
    DOCKER_LG_CLEANUP_TYPE_AUTO: str

class DockerManager(ResourceManager):
    def __attrs_post_init__(self) -> None: ...
    def on_resource_added(self, resource) -> None: ...
    def poll(self) -> None: ...

class DockerDaemon(ManagedResource):
    docker_daemon_url: Incomplete
    manager_cls = DockerManager
    timeout: float
    avail: bool
    def __attrs_post_init__(self) -> None: ...
    def on_client_bound(self, client) -> None: ...
    def on_poll(self, docker_client) -> None: ...
