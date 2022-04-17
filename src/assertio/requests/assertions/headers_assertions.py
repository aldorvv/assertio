"""Headers assertions module."""
from typing import Optional

from ..base_request import BaseRequest
from ...decorators import then

from truth.truth import AssertThat
from pydash import _


class HeadersAssertions(BaseRequest):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @then
    def assert_response_headers_contains(self, key: str):
        AssertThat(self.response.headers).Contains(key)

    @then
    def assert_response_headers_does_not_contain(self, key: str):
        AssertThat(self.response.headers).Contains(key)

    @then
    def assert_response_header(self, key: str):
        self._target = self.response.headers.get(key)

    @then
    def equals(self, value):
        AssertThat(self._target).IsEqualTo(value)

    @then
    def is_not_equal_to(self, value):
        AssertThat(self._target).IsNotEqualTo(value)
