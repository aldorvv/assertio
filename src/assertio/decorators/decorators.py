"""Decorators module."""
from functools import wraps

from loguru import logger

from ..bootstrap import _CLI


DEFAULTS = _CLI().get_config()
logger.add(DEFAULTS.logfile, format="{time} | {level} | {message}")


def given(fn):
    """Set a function as a given precondition."""

    def _(instance, *args, **kwargs):
        fn(instance, *args, **kwargs)
        return instance

    return _


def then(fn):
    """Set a function as a then action."""

    def _(instance, *args, **kwargs):
        msg = (
            f"{instance.method.upper()} {DEFAULTS.base_url}{instance.endpoint}"
        )
        try:
            fn(instance, *args, **kwargs)
            logger.success(f"PASSED {msg} {fn.__name__}")
        except AssertionError:
            logger.error(f"FAILED: {msg} {fn.__name__}")
        finally:
            return instance

    return _


def when(fn):
    """Set a function as a when assertion."""

    def _(instance, *args, **kwargs):
        fn(instance, *args, **kwargs)
        return instance

    return _


def log_test(fn):
    """Add a simple log message when a test starts."""
    def _(*args, **kwargs):
        logger.info(f"{fn.__name__} started")
        fn(*args, **kwargs)

    return _


def weight(value: int):
    """Add a function a weight attr."""
    def attr_decorator(fn):
        @wraps(fn)
        def _(*args, **kwargs):
            return fn(*args, **kwargs)

        setattr(_, "weight", value)
        return _

    return attr_decorator
