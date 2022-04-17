"""Assertio request module."""
from json import dumps
from requests import request

from ..decorators import when
from ..config import DEFAULTS
from .base_request import BaseRequest


class Actions(BaseRequest):
    """Assertio Request object."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @when
    def perform(self):
        """Execute request."""
        self.response = request(
            self.method,
            f"{DEFAULTS.base_url}{self.endpoint}",
            params=self.params,
            data=dumps(self.body),
            headers=self.headers,
        )
