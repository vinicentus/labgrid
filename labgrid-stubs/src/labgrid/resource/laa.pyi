from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import Resource as Resource

class LAASerialPort(Resource):
    laa_identity: Incomplete
    serial_name: Incomplete

class LAAPowerPort(Resource):
    laa_identity: Incomplete
    power_on: Incomplete
    power_off: Incomplete
    power_cycle: Incomplete
    def __attrs_post_init__(self) -> None: ...

class LAAUSBGadgetMassStorage(Resource):
    laa_identity: Incomplete
    image: Incomplete

class LAAUSBPort(Resource):
    laa_identity: Incomplete
    usb_ports: Incomplete

class LAAButtonPort(Resource):
    laa_identity: Incomplete
    buttons: Incomplete

class LAALed(Resource):
    laa_identity: Incomplete

class LAATempSensor(Resource):
    laa_identity: Incomplete

class LAAWattMeter(Resource):
    laa_identity: Incomplete

class LAAProvider(Resource):
    laa_identity: Incomplete
