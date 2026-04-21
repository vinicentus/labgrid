from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from .common import Driver as Driver

class USBAudioInputDriver(Driver):
    bindings: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def start_sender(self): ...
    @Driver.check_active
    def create_gst_src(self): ...
    @Driver.check_active
    def measure_level(self): ...
    @Driver.check_active
    def play(self): ...
