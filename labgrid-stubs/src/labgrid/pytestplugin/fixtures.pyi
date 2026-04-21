from collections.abc import Generator

from _typeshed import Incomplete

from ..exceptions import NoDriverFoundError as NoDriverFoundError
from ..exceptions import NoResourceFoundError as NoResourceFoundError
from ..logging import DEFAULT_FORMAT as DEFAULT_FORMAT
from ..remote.client import UserError as UserError
from ..resource.remote import RemotePlace as RemotePlace
from ..util.ssh import sshmanager as sshmanager
from .hooks import LABGRID_ENV_KEY as LABGRID_ENV_KEY

def pytest_addoption(parser) -> None: ...
def env(request, record_testsuite_property) -> Generator[Incomplete]: ...
def target(env): ...
def strategy(request, target): ...
