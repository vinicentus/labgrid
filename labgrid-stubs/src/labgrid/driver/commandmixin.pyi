from _typeshed import Incomplete

from ..step import step as step
from ..util import Timeout as Timeout
from .common import Driver as Driver
from .exception import ExecutionError as ExecutionError

class CommandMixin:
    def __attrs_post_init__(self) -> None: ...
    @Driver.check_active
    def wait_for(self, cmd, pattern, timeout: float = 30.0, sleepduration: int = 1) -> None: ...
    @Driver.check_active
    def poll_until_success(
        self,
        cmd,
        *,
        expected: int = 0,
        tries: Incomplete | None = None,
        timeout: float = 30.0,
        sleepduration: int = 1,
    ): ...
    @Driver.check_active
    def run_check(self, cmd: str, *, timeout: int = 30, codec: str = "utf-8", decodeerrors: str = "strict"): ...
