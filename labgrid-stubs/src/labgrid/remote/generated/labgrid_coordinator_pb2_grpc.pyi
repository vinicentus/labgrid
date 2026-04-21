"""Minimal stub so this package type-checks in isolation.

Full gRPC service definitions are bundled with the ``labgrid`` runtime package.
"""

from typing import Any

def __getattr__(name: str) -> Any: ...
