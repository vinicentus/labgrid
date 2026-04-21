from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .base import SerialPort as SerialPort
from .common import NetworkResource as NetworkResource
from .common import Resource as Resource

class RawSerialPort(SerialPort, Resource):
    def __attrs_post_init__(self) -> None: ...

class NetworkSerialPort(NetworkResource):
    port: Incomplete
    speed: Incomplete
    protocol: Incomplete
