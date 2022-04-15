"""Assertio request module."""
from http import HTTPStatus as HTTP
from typing import Dict, Union

from pydash import _
from requests import request
from truth.truth import AssertThat

from .decorators import given, then, when
from . import config

_defs = config.DEFAULTS


class Request:
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

    @when
    def perform(self):
        """Execute request."""
        self.response = request(
            self.method,
            f"{_defs.base_url}{self.endpoint}",
            params=self.params,
            data=self.body,
            headers=self.headers,
        )

    @then
    def assert_http_ok(self):
        """Assert response status is 200 OK."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.OK)

    @then
    def assert_http_created(self):
        """Assert response status is 201 CREATED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.CREATED)

    @then
    def assert_http_unauthorized(self):
        """Assert response status is 401 UNAUTHORIZED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.UNAUTHORIZED)

    @then
    def assert_response_contains(self, expected_key):
        """Assert response body contains key."""
        is_present = _.get(self.response.json(), expected_key)
        AssertThat(is_present).IsTruthy()

    @then
    def assert_that_response_field(self, target_key):
        """Set a target value to assert any other condition."""
        self.target = _.get(self.response.json(), target_key)

    @then
    def is_empty(self):
        """Assert target value is an empty array."""
        AssertThat(self.target).IsEmpty()

    @then
    def is_not_empty(self):
        """Assert target value is an empty array."""
        AssertThat(self.target).IsNotEmpty()

    @then
    def is_true(self):
        """Assert target value is true."""
        AssertThat(self.target).IsTrue()

    @then
    def is_false(self):
        """Assert target value is false."""
        AssertThat(self.target).IsFalse()

    @then
    def is_null(self):
        """Assert target value is null."""
        AssertThat(self.target).IsNone()

    @then
    def equals(self, expected_value):
        """Assert target value is null."""
        AssertThat(self.target).IsEqualTo(expected_value)

    @then
    def contains(self, expected_value):
        """Assert target value is null."""
        AssertThat(self.target).Contains(expected_value)

    @then
    def does_not_contain(self, expected_value):
        """Assert target value is null."""
        AssertThat(self.target).DoesNotContain(expected_value)
