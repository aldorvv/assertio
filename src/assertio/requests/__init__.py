"""Aliases and exports."""
from .action_request import Actions
from .precondition_request import Preconditions
from .assertions import BodyAssertions, HeadersAssertions, StatusAssertions


class __Request(
    Actions, BodyAssertions, HeadersAssertions, Preconditions, StatusAssertions
):
    ...


Request = __Request
AssertioRequest = __Request

__all__ = ("AssertioRequest", "Request")
