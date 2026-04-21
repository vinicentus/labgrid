import enum

from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from ..step import step as step
from .common import Strategy as Strategy
from .common import StrategyError as StrategyError
from .common import never_retry as never_retry

class Status(enum.Enum):
    unknown = 0
    off = 1
    shell = 2

class ShellStrategy(Strategy):
    bindings: Incomplete
    status: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @never_retry
    def transition(self, status, *, step) -> None: ...
    @never_retry
    def force(self, status, *, step) -> None: ...
