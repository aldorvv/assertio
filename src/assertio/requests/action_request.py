"""Assertio request module."""
from requests import request
from typing import Optional

from ..decorators import when
from ..config import DEFAULTS
from .base_request import BaseRequest


class Actions(BaseRequest):
    """Assertio Request object."""

    def __init__(
        self,
        method: Optional[str] = None,
        endpoint: Optional[str] = None
    ):
        super().__init__(method, endpoint)

    @when
    def perform(self):
        """Execute request."""
        self.response = request(
            self.method,
            f"{DEFAULTS.base_url}{self.endpoint}",
            params=self.params,
            data=self.body,
            headers=self.headers,
        )
