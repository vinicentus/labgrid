from _typeshed import Incomplete

from ..exceptions import NoConfigFoundError as NoConfigFoundError
from ..util.yaml import load as load

class ResourceConfig:
    filename: Incomplete
    template_env: Incomplete
    data: Incomplete
    def __attrs_post_init__(self) -> None: ...
