import enum
from typing import Any

from _typeshed import Incomplete

class StateError(Exception):
    msg: Incomplete

class BindingError(Exception):
    msg: Incomplete

class BindingState(enum.Enum):
    error = -1
    idle = 0
    bound = 1
    active = 2

class BindingMixin:
    bindings: dict[str, Any]
    target: Incomplete
    name: Incomplete
    state: Incomplete
    suppliers: Incomplete
    clients: Incomplete
    def __attrs_post_init__(self) -> None: ...
    @property
    def display_name(self): ...
    def on_supplier_bound(self, supplier) -> None: ...
    def on_client_bound(self, client) -> None: ...
    def on_activate(self) -> None: ...
    def on_deactivate(self) -> None: ...
    def resolve_conflicts(self, client) -> None: ...
    def get_bound_resources(self) -> None: ...
    @classmethod
    def check_active(cls, func): ...
    @classmethod
    def check_bound(cls, func): ...
    class NamedBinding:
        value: Incomplete
        def __init__(self, value) -> None: ...
