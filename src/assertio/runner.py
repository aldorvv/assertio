"""Test runner module."""


class Runner:
    """Test runner."""

    def start(self, *args):
        """Run all tests on a runner.

        Tests function names must start with 'test'.
        """
        [getattr(self, fn)(*args) for fn in dir(self) if fn.startswith("test")]
