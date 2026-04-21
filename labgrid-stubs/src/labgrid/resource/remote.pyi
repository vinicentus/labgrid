from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import ManagedResource as ManagedResource
from .common import NetworkResource as NetworkResource
from .common import ResourceManager as ResourceManager

class RemotePlaceManager(ResourceManager):
    url: Incomplete
    loop: Incomplete
    session: Incomplete
    ready: Incomplete
    unmanaged_resources: Incomplete
    def __attrs_post_init__(self) -> None: ...
    env: Incomplete
    def on_resource_added(self, resource) -> None: ...
    def poll(self) -> None: ...

class RemotePlace(ManagedResource):
    manager_cls = RemotePlaceManager
    timeout: float
    tags: Incomplete
    def __attrs_post_init__(self) -> None: ...

class RemoteUSBResource(NetworkResource, ManagedResource):
    manager_cls = RemotePlaceManager
    busnum: Incomplete
    devnum: Incomplete
    path: Incomplete
    vendor_id: Incomplete
    model_id: Incomplete

class RemoteAndroidUSBFastboot(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkAndroidFastboot(RemoteAndroidUSBFastboot):
    def __attrs_post_init__(self) -> None: ...

class RemoteAndroidNetFastboot(NetworkResource):
    address: Incomplete
    port: Incomplete
    protocol: Incomplete

class NetworkDFUDevice(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkIMXUSBLoader(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkMXSUSBLoader(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkRKUSBLoader(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkAlteraUSBBlaster(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkSigrokUSBDevice(RemoteUSBResource):
    driver: Incomplete
    channels: Incomplete
    channel_group: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkSigrokUSBSerialDevice(RemoteUSBResource):
    driver: Incomplete
    channels: Incomplete
    channel_group: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBMassStorage(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBSDMuxDevice(RemoteUSBResource):
    control_path: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBSDWireDevice(RemoteUSBResource):
    control_serial: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBSDWire3Device(RemoteUSBResource):
    control_serial: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkSiSPMPowerPort(RemoteUSBResource):
    index: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBPowerPort(RemoteUSBResource):
    index: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBVideo(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBAudioInput(RemoteUSBResource):
    index: Incomplete
    alsa_name: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBTMC(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBDebugger(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkDeditecRelais8(RemoteUSBResource):
    index: Incomplete
    invert: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkHIDRelay(RemoteUSBResource):
    index: Incomplete
    invert: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkSysfsGPIO(NetworkResource, ManagedResource):
    manager_cls = RemotePlaceManager
    index: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkLXAIOBusNode(ManagedResource):
    manager_cls = RemotePlaceManager
    host: Incomplete
    node: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkLXAIOBusPIO(NetworkLXAIOBusNode):
    pin: Incomplete
    invert: Incomplete

class NetworkLXAUSBMux(RemoteUSBResource):
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class NetworkUSBFlashableDevice(RemoteUSBResource):
    devnode: Incomplete

class NetworkMQTTResource(ManagedResource):
    manager_cls = RemotePlaceManager
    host: Incomplete
    avail_topic: Incomplete
    timeout: float
    def __attrs_post_init__(self) -> None: ...

class RemoteNetworkInterface(NetworkResource, ManagedResource):
    manager_cls = RemotePlaceManager
    ifname: Incomplete

class RemoteBaseProvider(NetworkResource):
    internal: Incomplete
    external: Incomplete

class RemoteTFTPProvider(RemoteBaseProvider): ...
class RemoteNFSProvider(NetworkResource): ...
class RemoteHTTPProvider(RemoteBaseProvider): ...
