"""Preconditions module."""
from typing import Dict, Union

from ..types import Headers, Cookies
from ..decorators import given
from .base_request import BaseRequest


class Preconditions(BaseRequest):
    """Precondition methods."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @given
    def to(self, endpoint: str, **kwargs):
        """Set endpoint to request."""
        self.endpoint = endpoint
        if kwargs:
            self.endpoint = self.endpoint.format(**kwargs)

    @given
    def with_method(self, method: str):
        """Set HTTP request method."""
        self.method = method

    @given
    def with_body(self, body: Union[Dict, str]):
        """Set request Content-Type: appliaction/json body."""
        self.body = body

    @given
    def with_headers(self, headers: Headers):
        """Set request header or headers."""
        self.headers = headers
    
    @given
    def with_params(self, params: Dict):
        """Set request query parameters."""
        self.params = params

    @given
    def with_header(self, *args):
        """Set only a header using a string or key, value pair.

        Examples
        --------
        .with_header("Content-Type", "application/json")\
        .with_header("Authorization=Bearer <token>")

        """
        if self.headers is None:
            self.headers = {}

        if len(args) == 1:
            key, value = args[0].split("=")
        else:
            key, value = args
        self.headers.update({key: value})

    @given
    def with_cookies(self, cookies: Cookies):
        """Set a cookies dictionary.
        

        Examples
        --------
        .with_cookies({"Cookie": "Value"})

        """
        self.cookies = cookies

    @given
    def with_cookie(self, *args):
        """Set only a cookie using a string or key, value pair.

        Examples
        --------
        .with_cookie("Session", "value")\
        .with_cookie("X-CustomCookie=value")

        """
        if self.cookies is None:
            self.cookies = {}

        if len(args) == 1:
            key, value = args[0].split("=")
        else:
            key, value = args
        self.cookies.update({key: value})

    @given
    def with_bearer_token(self, token: str):
        """Setup Authorization header using bearer token.
        
        If token does not contain "Bearer " this method
        adds it.

        Examples
        --------
        .with_bearer_token("<token>")\
        .perform()

        """
        if "Bearer " not in token:
            token = f"Bearer {token}"
        self.with_header("Authorization", token)

    @given
    def with_content_type(self, content_type: str):
        """Shortcut to add content-type header."""
        self.with_header("Content-Type", content_type)

    @given
    def with_application_json(self):
        """Shortcut to set content-type to application/json."""
        self.with_headers("Content-Type", "application/json")