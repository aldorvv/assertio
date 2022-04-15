"""Test runner module."""
from .decorators import log_test


class Runner:
    """Test runner."""

    def start(self, *args):
        """Run all tests on a runner.

        Tests function names must start with 'test'.
        """
        for fn in filter(lambda fn: fn.startswith("test"), dir(self)):
            log_test(getattr(self, fn))(*args)
