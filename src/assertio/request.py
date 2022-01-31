from os import getenv
from http import HTTPStatus as HTTP

from pydash import _
from requests import request
from truth.truth import AssertThat

from .decorators import given, then, when


class Request:
    BASE_URL = getenv("ASSERTIO_BASE_URL", "http://127.0.0.1")

    def __init__(self):
        self.body = None
        self.headers = None
        self.params = None

    @given
    def to(self, endpoint, **kwargs):
        self.endpoint = endpoint
        if kwargs:
            self.endpoint = self.endpoint.format(**kwargs)

    @given
    def with_method(self, method):
        self.method = method
    
    @given
    def with_body(self, body):
        self.body = body

    @given
    def with_headers(self, headers):
        self.headers = headers

    @given
    def with_params(self, params):
        self.params = params
    
    @when
    def perform(self):
        self.request = request(
            self.method, 
            f"{self.BASE_URL}{self.endpoint}", 
            params=self.params, 
            data=self.body, 
            headers=self.headers
        )

    @then
    def assert_http_ok(self):
        AssertThat(self.request.status_code).IsEqualTo(HTTP.OK)
    
    @then
    def assert_http_created(self):
        AssertThat(self.request.status_code).IsEqualTo(HTTP.CREATED)

    @then
    def assert_http_unauthorized(self):
        AssertThat(self.request.status_code).IsEqualTo(HTTP.UNAUTHORIZED)

    @then
    def assert_response_contains(self, expected_key):
        is_present = _.get(self.request.json(), expected_key)
        AssertThat(is_present).IsTruthy()
    
    @then
    def assert_that_response_field(self, target_key):
        self.target = _.get(self.request.json(), target_key)

    @then
    def is_empty(self):
        AssertThat(self.target).IsEmpty()

    @then
    def is_true(self):
        AssertThat(self.target).IsTrue()

    @then
    def is_false(self):
        AssertThat(self.target).IsFalse()
    
    @then
    def is_null(self):
        AssertThat(self.target).IsNone()
