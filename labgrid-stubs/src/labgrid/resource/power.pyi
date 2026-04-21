from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import Resource as Resource

class NetworkPowerPort(Resource):
    model: Incomplete
    host: Incomplete
    index: Incomplete

class PDUDaemonPort(Resource):
    host: Incomplete
    pdu: Incomplete
    index: Incomplete
