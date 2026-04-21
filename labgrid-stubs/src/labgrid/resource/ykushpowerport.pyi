from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import NetworkResource as NetworkResource
from .common import Resource as Resource

class YKUSHPowerPort(Resource):
    serial: Incomplete
    index: Incomplete

class NetworkYKUSHPowerPort(NetworkResource):
    serial: Incomplete
    index: Incomplete
