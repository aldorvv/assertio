"""Test runner module."""
from .decorators import log_test
from .types import MethodsList

class Runner:
    """Test runner."""

    def start(self, *args):
        """Run all tests on a runner.

        Tests function names must start with 'test'.
        """
        methods = self.__get_tests()
        with_weight = self.__sort_by_weight(methods)
    
        for fn in with_weight:
            log_test(fn)(*args)

    def __get_tests(self) -> MethodsList:
        """Get each runner test methods."""
        names = filter(lambda fn: fn.startswith("test"), dir(self))
        return [getattr(self, fn) for fn in names]

    def __sort_by_weight(self, methods: MethodsList) -> MethodsList:
        """Sort methods based on it's weight."""
        for method in methods:
            if not hasattr(method, "weight"):
                setattr(method, "weight", 0)
        return sorted(methods, key=lambda fn: fn.weight, reverse=True)

