from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import Resource as Resource

class SigrokDevice(Resource):
    driver: Incomplete
    channels: Incomplete
    channel_group: Incomplete
