from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from ..util import gen_marker as gen_marker
from ..util import re_vt100 as re_vt100
from .common import Driver as Driver
from .ubootdriver import UBootDriver as UBootDriver

class SmallUBootDriver(UBootDriver):
    boot_expression: Incomplete
    boot_secret: Incomplete
    boot_secret_nolf: Incomplete
    login_timeout: Incomplete
    @Driver.check_active
    def boot(self, name) -> None: ...
