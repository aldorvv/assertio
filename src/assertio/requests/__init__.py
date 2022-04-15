"""Aliases and exports."""
from .action_request import ActionRequest
from .precondition_request import PreconditionRequest
from .assertions import BodyAssertions, StatusAssertions


class __Request(
    ActionRequest, BodyAssertions, PreconditionRequest, StatusAssertions
):
    ...


Request = __Request
AssertioRequest = __Request

__all__ = ("AssertioRequest", "Request")
