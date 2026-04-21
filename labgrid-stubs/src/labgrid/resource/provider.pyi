from _typeshed import Incomplete

from ..factory import target_factory as target_factory
from .common import Resource as Resource

class BaseProvider(Resource):
    internal: Incomplete
    external: Incomplete
    host: str
    def __attrs_post_init__(self) -> None: ...

class TFTPProvider(BaseProvider): ...

class NFSProvider(Resource):
    host: str
    def __attrs_post_init__(self) -> None: ...

class HTTPProvider(BaseProvider): ...
