import multiprocessing

from _typeshed import Incomplete

from .. import Environment as Environment
from .. import target_factory as target_factory
from ..exceptions import NoResourceFoundError as NoResourceFoundError
from ..logging import StepLogger as StepLogger
from ..logging import basicConfig as basicConfig

class Handler(multiprocessing.Process):
    env: Incomplete
    args: Incomplete
    config: Incomplete
    name: Incomplete
    context: Incomplete
    def __init__(self, env, args, name) -> None: ...
    log: Incomplete
    target: Incomplete
    setup: Incomplete
    initial_resource: Incomplete
    handler: Incomplete
    def run(self) -> None: ...
    def run_once(self): ...

class Manager:
    env: Incomplete
    args: Incomplete
    config: Incomplete
    log: Incomplete
    def __init__(self, env, args) -> None: ...
    handlers: Incomplete
    def configure(self): ...
    def start(self) -> None: ...
    def join(self) -> None: ...

def main() -> None: ...
