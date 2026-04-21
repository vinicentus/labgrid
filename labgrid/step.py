from __future__ import annotations

import inspect
import os
import warnings
from collections.abc import Callable, Sequence
from functools import wraps
from time import monotonic
from typing import Any, TypeVar, cast

_F = TypeVar("_F", bound=Callable[..., Any])


# TODO: collect events from all Steps and combine when possible, only flush
# after some time
class Steps:
    _stack: list[Step]
    _subscribers: list[Callable[[StepEvent], object]]

    def __init__(self) -> None:
        self._stack = []
        self._subscribers = []

    def get_current(self) -> Step | None:
        return self._stack[-1] if self._stack else None

    def get_new(
        self,
        title: str,
        tag: str | None,
        source: object | None,
        sourceinfo: tuple[str, str, int],
    ) -> Step:
        step = Step(title, level=len(self._stack) + 1, tag=tag, source=source, sourceinfo=sourceinfo)  # pylint: disable=redefined-outer-name
        return step

    def push(self, step: Step) -> None:  # pylint: disable=redefined-outer-name
        assert step not in self._stack
        self._stack.append(step)
        step.parent = self.get_current()
        step.level = len(self._stack)

    def pop(self, step: Step) -> None:  # pylint: disable=redefined-outer-name
        assert self._stack[-1] is step
        self._stack.pop()

    def subscribe(self, callback: Callable[[StepEvent], object]) -> None:
        self._subscribers.append(callback)

    def unsubscribe(self, callback: Callable[[StepEvent], object]) -> None:
        assert callback in self._subscribers
        self._subscribers.remove(callback)

    def notify(self, event: StepEvent) -> None:
        # TODO: buffer and try to merge consecutive events
        for subscriber in self._subscribers:
            try:
                subscriber(event)
            except Exception as e:  # pylint: disable=broad-except
                warnings.warn(
                    f"unhandled exception during event notification: {e}",
                    stacklevel=2,
                )


steps: Steps = Steps()


class StepEvent:
    ts: float | None
    step: Step | None
    data: dict[str, Any] | None
    resource: object | None
    stream: bool | None

    def __init__(
        self,
        current_step: Step,
        data: dict[str, Any],
        *,
        resource: object | None = None,
        stream: bool = False,
    ) -> None:
        self.ts = monotonic()  # used to keep track of the events age
        self.step = current_step
        self.data = data
        self.resource = resource
        self.stream = stream

    def __str__(self) -> str:
        result = [self.step.title]
        if self.resource:
            result.append(self.resource.__class__.__name__)
        data = self.data.copy()
        duration = data.pop("duration", 0.0)
        pairs = [f"{k}={repr(v)}" for k, v in data.items() if v is not None]
        if duration >= 0.001:
            pairs.append(f"duration={duration:.3f}")
        result.append(", ".join(pairs))
        return " ".join(result)

    def __setitem__(self, k: str, v: Any) -> None:
        assert self.data is not None
        self.data[k] = v

    def _invalidate(self) -> None:
        self.ts = None
        self.step = None
        self.data = None
        self.resource = None
        self.stream = None

    def merge(self, other: StepEvent) -> bool:
        if not self.stream and not other.stream:
            return False
        assert self.ts is not None and other.ts is not None
        if self.ts > other.ts:
            return False
        if self.resource is not other.resource:
            return False
        if self.data.keys() != other.data.keys():
            return False
        assert self.data is not None and other.data is not None
        for k, v in other.data.items():
            self.data[k] += v
        other._invalidate()
        return True

    @property
    def age(self) -> float:
        assert self.ts is not None
        return monotonic() - self.ts


# TODO: allow attaching log information, using a Resource as meta-data
class Step:
    parent: Step | None
    args: dict[str, Any] | None
    result: Any
    exception: BaseException | None
    _start_ts: float | None
    _stop_ts: float | None
    _skipped: bool

    def __init__(
        self,
        title: str,
        level: int,
        tag: str | None,
        source: object | None,
        sourceinfo: tuple[str, str, int],
    ) -> None:
        self.title = title
        self.level = level
        self.tag = tag
        self.source = source
        self.sourceinfo = sourceinfo
        self.args = None
        self.result = None
        self.exception = None
        self._start_ts = None
        self._stop_ts = None
        self._skipped = False

    def __repr__(self) -> str:
        result = [f"Step(title={self.title!r}, level={self.level}, status={self.status}"]
        if self.args is not None:
            result.append(f", args={self.args}")
        if self.exception is not None:
            result.append(f", exception={self.exception}")
        if self.result is not None:
            result.append(f", result={self.result}")
        duration = self.duration
        if duration >= 0.001:
            result.append(f", duration={duration:.3f}")
        result.append(")")
        return "".join(result)

    @property
    def duration(self) -> float:
        if self._start_ts is None:
            return 0.0
        if self._stop_ts is None:
            return monotonic() - self._start_ts

        return self._stop_ts - self._start_ts

    @property
    def status(self) -> str:
        if self._start_ts is None:
            return "new"
        if self._stop_ts is None:
            return "active"

        return "done"

    @property
    def is_active(self) -> bool:
        return self.status == "active"

    @property
    def is_done(self) -> bool:
        return self.status == "done"

    def _notify(self, event: StepEvent) -> None:
        assert event.step is self
        steps.notify(event)

    def start(self) -> None:
        assert self._start_ts is None
        self._start_ts = monotonic()
        steps.push(self)
        self._notify(
            StepEvent(
                self,
                {
                    "state": "start",
                    "args": self.args,
                },
            )
        )

    def skip(self, reason: str) -> None:
        assert self._start_ts is not None
        self._notify(StepEvent(self, {"skip": reason}))

    def stop(self) -> None:
        assert self._start_ts is not None
        assert self._stop_ts is None
        self._stop_ts = monotonic()
        event = StepEvent(self, {"state": "stop"})
        if self.exception:
            event["exception"] = self.exception
        else:
            event["result"] = self.result
        duration = self.duration
        if duration:
            event["duration"] = duration
        self._notify(event)
        steps.pop(self)

    def __del__(self) -> None:
        if not self.is_done:
            warnings.warn(f"__del__ called before {self!r} was done", stacklevel=2)


def step(
    *,
    title: str | None = None,
    args: Sequence[str] | None = None,
    result: bool = False,
    tag: str | None = None,
) -> Callable[[_F], _F]:
    if args is None:
        args_list: list[str] = []
    else:
        args_list = list(args)

    def decorator(func: _F) -> _F:
        resolved_title: str = title if title is not None else func.__name__

        signature = inspect.signature(func)

        @wraps(func)
        def wrapper(*_args: Any, **_kwargs: Any) -> Any:
            bound = signature.bind_partial(*_args, **_kwargs)
            bound.apply_defaults()
            source = func.__self__ if inspect.ismethod(func) else bound.arguments.get("self")
            pathname = func.__code__.co_filename
            sourceinfo = (pathname, os.path.basename(pathname), func.__code__.co_firstlineno)
            step = steps.get_new(resolved_title, tag, source, sourceinfo)  # pylint: disable=redefined-outer-name
            # optionally pass the step object
            if "step" in signature.parameters:
                _kwargs["step"] = step
            if args_list:
                step.args = {k: bound.arguments[k] for k in args_list}
            step.start()
            try:
                _result = func(*_args, **_kwargs)
                if result:
                    step.result = _result
            except Exception as e:
                step.exception = e
                raise
            finally:
                step.stop()
            return _result

        wrapper.__signature__ = signature.replace(
            parameters=[p for p in signature.parameters.values() if p.name != "step"]
        )
        return cast(_F, wrapper)

    return decorator
