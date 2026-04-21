from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import NetworkResource as NetworkResource
from .common import Resource as Resource

class Flashrom(Resource):
    programmer: Incomplete

class NetworkFlashrom(NetworkResource):
    programmer: Incomplete
