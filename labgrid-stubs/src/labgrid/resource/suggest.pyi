from _typeshed import Incomplete

from ..util import dump as dump
from .udev import USBTMC as USBTMC
from .udev import AlteraUSBBlaster as AlteraUSBBlaster
from .udev import AndroidUSBFastboot as AndroidUSBFastboot
from .udev import DFUDevice as DFUDevice
from .udev import HIDRelay as HIDRelay
from .udev import IMXUSBLoader as IMXUSBLoader
from .udev import LXAUSBMux as LXAUSBMux
from .udev import MatchedSysfsGPIO as MatchedSysfsGPIO
from .udev import RKUSBLoader as RKUSBLoader
from .udev import SiSPMPowerPort as SiSPMPowerPort
from .udev import USBAudioInput as USBAudioInput
from .udev import USBDebugger as USBDebugger
from .udev import USBMassStorage as USBMassStorage
from .udev import USBNetworkInterface as USBNetworkInterface
from .udev import USBPowerPort as USBPowerPort
from .udev import USBSDMuxDevice as USBSDMuxDevice
from .udev import USBSDWire3Device as USBSDWire3Device
from .udev import USBSDWireDevice as USBSDWireDevice
from .udev import USBSerialPort as USBSerialPort
from .udev import USBVideo as USBVideo

class Suggester:
    resources: Incomplete
    log: Incomplete
    def __init__(self, args) -> None: ...
    def suggest_callback(self, resource, meta, suggestions) -> None: ...
    def run(self) -> None: ...

def main() -> None: ...
