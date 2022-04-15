"""Decorators module."""
from loguru import logger

from ..config import DEFAULTS

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
