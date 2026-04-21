from _typeshed import Incomplete

from ..exception import ExecutionError as ExecutionError

PORT: int
MIN_OUTLET_INDEX: int
MAX_OUTLET_INDEX: int
HEADERS: Incomplete

def power_set(host, port, index, value) -> None: ...
def power_get(host, port, index): ...
