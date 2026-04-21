from __future__ import annotations

# ruff: noqa: I001
# Import order matters: load Target before Environment to avoid a circular import
# via Environment → Config → util → driver.
from .target import Target
from .environment import Environment
from .exceptions import NoConfigFoundError
from .factory import target_factory
from .step import step, steps
from .stepreporter import StepReporter
from .consoleloggingreporter import ConsoleLoggingReporter

__all__ = [
    "ConsoleLoggingReporter",
    "Environment",
    "NoConfigFoundError",
    "StepReporter",
    "Target",
    "__version__",
    "step",
    "steps",
    "target_factory",
]

try:
    from ._version import __version__ as __version__
except ImportError:
    __version__: str = "unknown"
