from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import Resource as Resource

class ModbusTCPCoil(Resource):
    host: Incomplete
    coil: Incomplete
    invert: Incomplete
    write_multiple_coils: Incomplete

class WaveshareModbusTCPCoil(ModbusTCPCoil):
    coil_count: Incomplete
