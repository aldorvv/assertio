"""Body assertions module."""
from typing import Optional

from ..base_request import BaseRequest
from ...decorators import then

from truth.truth import AssertThat
from pydash import _


class BodyAssertions(BaseRequest):
    """Content-Type: Application/json responses assertions."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @then
    def assert_response_contains(self, expected_key):
        """Assert response body contains key."""
        is_present = _.get(self.response.json(), expected_key)
        AssertThat(is_present).IsTruthy()

    @then
    def assert_response_field(self, target_key):
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

    @then
    def is_equal_to_request_payload_field(self, key: str):
        """Asserts target value equals to Request().body key."""
        AssertThat(self.target).IsEqualTo(_.get(self.body, key))

    @then
    def is_not_equal_to_request_payload_field(self, key: str):
        """Asserts target value is not equal to Request().body key."""
        AssertThat(self.target).IsNotEqualTo(_.get(self.body, key))
