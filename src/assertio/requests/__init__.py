"""Aliases and exports."""
from .action_request import Actions
from .precondition_request import Preconditions
from .assertions import BodyAssertions, StatusAssertions


class __Request(
    Actions, BodyAssertions, Preconditions, StatusAssertions
):
    ...


Request = __Request
AssertioRequest = __Request

__all__ = ("AssertioRequest", "Request")
