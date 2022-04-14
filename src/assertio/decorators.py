from loguru import logger

from . import config

__defs = config.DEFAULTS


def given(fn):
    def wrapped_given(instance, *args, **kwargs):
        fn(instance, *args, **kwargs)
        return instance

    return wrapped_given


def then(fn):
    def wrapped_then(instance, *args, **kwargs):
        msg = f"{instance.method.upper()} {__defs.base_url}{instance.endpoint}"
        try:
            fn(instance, *args, **kwargs)
            logger.success(f"{fn.__name__} PASSED {msg}")
        except AssertionError:
            logger.error(f"{fn.__name__} FAILED: {msg}")
        finally:
            return instance

    return wrapped_then


def when(fn):
    def wrapped_when(instance, *args, **kwargs):
        fn(instance, *args, **kwargs)
        return instance

    return wrapped_when
