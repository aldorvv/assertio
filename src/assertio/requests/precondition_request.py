"""Assertio request module."""
from typing import Dict, Union

from ..decorators import given
from .base_request import BaseRequest


class PreconditionRequest(BaseRequest):
    """Assertio Request object."""

    def __init__(self):
        """Class constructor."""
        self.body: Union[Dict, None] = None
        self.headers: Union[Dict, None] = None
        self.params: Union[Dict, None] = None

    @given
    def to(self, endpoint, **kwargs):
        """Set endpoint to request."""
        self.endpoint = endpoint
        if kwargs:
            self.endpoint = self.endpoint.format(**kwargs)

    @given
    def with_method(self, method):
        """Set HTTP request method."""
        self.method = method

    @given
    def with_body(self, body):
        """Set request Content-Type: appliaction/json body."""
        if self.body is None:
            self.body = body
        else:
            self.body.update(body)

    @given
    def with_headers(self, headers):
        """Set request header or headers."""
        if self.headers is None:
            self.headers = headers
        else:
            self.headers.update(headers)

    @given
    def with_params(self, params):
        """Set request query parameters."""
        if self.params is None:
            self.params = params
        else:
            self.params.update(params)
