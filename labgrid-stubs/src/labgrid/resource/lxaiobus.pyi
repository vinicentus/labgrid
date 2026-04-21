from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import ManagedResource as ManagedResource
from .common import ResourceManager as ResourceManager

class LXAIOBusNodeManager(ResourceManager):
    def __attrs_post_init__(self) -> None: ...
    def poll(self) -> None: ...

class LXAIOBusNode(ManagedResource):
    manager_cls = LXAIOBusNodeManager
    host: Incomplete
    node: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class LXAIOBusPIO(LXAIOBusNode):
    pin: Incomplete
    invert: Incomplete
