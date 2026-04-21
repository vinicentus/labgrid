from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .base import SerialPort as SerialPort
from .common import Resource as Resource

class ModbusRTU(SerialPort, Resource):
    address: Incomplete
    timeout: Incomplete
    def __attrs_post_init__(self) -> None: ...
