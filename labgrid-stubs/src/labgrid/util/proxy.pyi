from _typeshed import Incomplete

from ..resource.common import Resource as Resource
from .ssh import sshmanager as sshmanager

class ProxyError(Exception): ...

class ProxyManager:
    @classmethod
    def force_proxy(cls, force_proxy) -> None: ...
    @classmethod
    def get_host_and_port(cls, res, *, default_port=None, force_port=None): ...
    @classmethod
    def get_url(cls, url, *, default_port=None): ...
    @classmethod
    def get_grpc_address(cls, address, *, default_port=None): ...
    @classmethod
    def get_command(cls, res, host, port, ifname=None): ...

proxymanager: Incomplete
