from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import Resource as Resource

class SerialPort(Resource):
    port: Incomplete
    speed: Incomplete

class NetworkInterface(Resource):
    ifname: Incomplete

class EthernetPort(Resource):
    switch: Incomplete
    interface: Incomplete

class SysfsGPIO(Resource):
    index: Incomplete
