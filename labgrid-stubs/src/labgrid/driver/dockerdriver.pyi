from enum import Enum

from _typeshed import Incomplete

from labgrid.driver.common import Driver as Driver
from labgrid.factory import target_factory as target_factory
from labgrid.protocol.powerprotocol import PowerProtocol as PowerProtocol
from labgrid.resource.docker import DockerConstants as DockerConstants

class PullPolicy(Enum):
    Always = "always"
    Missing = "missing"
    Never = "never"

def pull_policy_converter(value): ...

class DockerDriver(PowerProtocol, Driver):
    bindings: Incomplete
    image_uri: Incomplete
    pull: Incomplete
    command: Incomplete
    volumes: Incomplete
    container_name: Incomplete
    environment: Incomplete
    host_config: Incomplete
    network_services: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    def on(self) -> None: ...
    def off(self) -> None: ...
    def cycle(self) -> None: ...
