"""Assertio request module."""
from json import dumps
from requests import request

from ..decorators import when
from ..bootstrap import _CLI
from .base_request import BaseRequest


DEFAULTS = _CLI().get_config()

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
            cookies=self.cookies,
            params=self.params,
            data=dumps(self.body),
            headers=self.headers,
        )
