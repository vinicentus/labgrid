from ...util.snmp import SimpleSNMP as SimpleSNMP
from ..exception import ExecutionError as ExecutionError

OID: str
NUMBER_OF_OUTLETS: int

def power_set(host, port, index, value) -> None: ...
def power_get(host, port, index): ...
