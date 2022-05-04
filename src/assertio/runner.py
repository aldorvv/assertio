"""Test runner module."""
from .decorators import log_test
from .types import MethodList, TestMethod, TestMethods

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

    def __get_tests(self) -> TestMethods:
        """Get each runner test methods."""
        names = filter(lambda fn: fn.startswith("test"), dir(self))
        methods: TestMethods = []
        for name in names:
            fn = getattr(self, name)
            weight = getattr(fn, "weight", 0)
            methods.append(TestMethod(fn, weight))
        return methods

    def __sort_by_weight(self, methods: TestMethods) -> MethodList:
        """Sort methods based on it's weight."""
        sorted_ = sorted(methods, key=lambda test: test.weight, reverse=True)
        return [test.function for test in sorted_]

