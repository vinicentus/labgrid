from _typeshed import Incomplete

class QMPMonitor:
    monitor_out: Incomplete
    monitor_in: Incomplete
    logger: Incomplete
    def __attrs_post_init__(self) -> None: ...
    def execute(self, command, arguments={}): ...

class QMPError(Exception):
    msg: Incomplete
