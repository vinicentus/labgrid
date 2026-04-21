from _typeshed import Incomplete

from ..driver.exception import ExecutionError as ExecutionError

class SimpleSNMP:
    engine: Incomplete
    transport: Incomplete
    community: Incomplete
    context: Incomplete
    def __init__(self, host, community, port: int = 161) -> None: ...
    def get(self, oid): ...
    def set(self, oid, value) -> None: ...
