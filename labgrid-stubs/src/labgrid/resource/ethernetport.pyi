from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import ManagedResource as ManagedResource
from .common import ResourceManager as ResourceManager

class SNMPSwitch:
    hostname: Incomplete
    logger: Incomplete
    ports: Incomplete
    fdb: Incomplete
    macs_by_port: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def update(self) -> None: ...

class EthernetPortManager(ResourceManager):
    loop: Incomplete
    poll_tasks: Incomplete
    switches: Incomplete
    neighbors: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_resource_added(self, resource) -> None: ...
    def poll(self) -> None: ...

class SNMPEthernetPort(ManagedResource):
    manager_cls = EthernetPortManager
    switch: Incomplete
    interface: Incomplete
    extra: Incomplete
    def __attrs_post_init__(self) -> None: ...
