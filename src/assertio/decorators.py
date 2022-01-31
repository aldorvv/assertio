from os import getenv
from http import HTTPStatus as HTTP

from loguru import logger

BASE_URL = getenv("ASSERTIO_BASE_URL", "http://127.0.0.1")
LOGFILE = getenv("ASSERTIO_LOGFILE", "assertio.log")

logger.add(LOGFILE, format="{level} | {message}")


def given(func):
    def wrapped_given(instance, *args, **kwargs):
        func(instance, *args, **kwargs)
        return instance
    return wrapped_given

def then(func):
    def wrapped_then(instance, *args, **kwargs):
        info = f"{instance.method.upper()} {BASE_URL}{instance.endpoint}"
        try:
            func(instance, *args, **kwargs)
            logger.success(f"{func.__name__} PASSED {info}")
        except AssertionError:
            logger.error(f"{func.__name__} FAILED: {info}")
        finally:
            return instance
    return wrapped_then

def when(func):
    def wrapped_when(instance, *args, **kwargs):
        func(instance, *args, **kwargs)
        return instance
    return wrapped_when