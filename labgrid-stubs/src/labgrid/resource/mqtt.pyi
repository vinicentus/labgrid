from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import ManagedResource as ManagedResource
from .common import ResourceManager as ResourceManager

class MQTTManager(ResourceManager):
    def on_resource_added(self, resource) -> None: ...
    def poll(self) -> None: ...

class MQTTResource(ManagedResource):
    manager_cls = MQTTManager
    host: Incomplete
    avail_topic: Incomplete
    username: Incomplete
    password: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class TasmotaPowerPort(MQTTResource):
    power_topic: Incomplete
    status_topic: Incomplete
