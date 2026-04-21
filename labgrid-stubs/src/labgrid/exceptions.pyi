from _typeshed import Incomplete

class NoConfigFoundError(Exception):
    msg: Incomplete

class NoSupplierFoundError(Exception):
    msg: Incomplete
    filter: Incomplete

class InvalidConfigError(Exception):
    msg: Incomplete

class NoDriverFoundError(NoSupplierFoundError): ...

class NoResourceFoundError(NoSupplierFoundError):
    found: Incomplete

class NoStrategyFoundError(NoSupplierFoundError): ...

class RegistrationError(Exception):
    msg: Incomplete
