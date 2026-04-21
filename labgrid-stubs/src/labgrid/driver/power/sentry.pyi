from _typeshed import Incomplete

from ...util.helper import processwrapper as processwrapper
from ..exception import ExecutionError as ExecutionError

INDEX_TO_OID: Incomplete
BASE_STATUS_OID: str
BASE_CTRL_OID: str

def power_set(host, port, index, value) -> None: ...
def power_get(host, port, index): ...
