import enum

from _typeshed import Incomplete

from ..driver.dockerdriver import DockerDriver as DockerDriver
from ..factory import target_factory as target_factory
from ..step import step as step
from .common import Strategy as Strategy
from .common import StrategyError as StrategyError
from .common import never_retry as never_retry

class Status(enum.Enum):
    unknown = 0
    gone = 1
    accessible = 2

class DockerStrategy(Strategy):
    bindings: Incomplete
    status: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @never_retry
    def transition(self, status) -> None: ...
