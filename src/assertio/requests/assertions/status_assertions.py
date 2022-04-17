"""HTTP status module."""
from http import HTTPStatus as HTTP
from typing import Optional

from truth.truth import AssertThat

from ...decorators import then
from ..base_request import BaseRequest


class StatusAssertions(BaseRequest):
    """HTTP status assertions."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @then
    def assert_http_continue(self):
        """Assert response status is 100 CONTINUE."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.CONTINUE)

    @then
    def assert_http_switching_protocols(self):
        """Assert response status is 101 SWITCHING_PROTOCOLS."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.SWITCHING_PROTOCOLS
        )

    @then
    def assert_http_processing(self):
        """Assert response status is 102 PROCESSING."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.PROCESSING)

    @then
    def assert_http_early_hints(self):
        """Assert response status is 103 EARLY_HINTS."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.EARLY_HINTS)

    @then
    def assert_http_ok(self):
        """Assert response status is 200 OK."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.OK)

    @then
    def assert_http_created(self):
        """Assert response status is 201 CREATED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.CREATED)

    @then
    def assert_http_accepted(self):
        """Assert response status is 202 ACCEPTED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.ACCEPTED)

    @then
    def assert_http_non_authoritative_information(self):
        """Assert response status is 203 NON_AUTHORITATIVE_INFORMATION."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.NON_AUTHORITATIVE_INFORMATION
        )

    @then
    def assert_http_no_content(self):
        """Assert response status is 204 NO_CONTENT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.NO_CONTENT)

    @then
    def assert_http_reset_content(self):
        """Assert response status is 205 RESET_CONTENT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.RESET_CONTENT)

    @then
    def assert_http_partial_content(self):
        """Assert response status is 206 PARTIAL_CONTENT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.PARTIAL_CONTENT)

    @then
    def assert_http_multi_status(self):
        """Assert response status is 207 MULTI_STATUS."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.MULTI_STATUS)

    @then
    def assert_http_already_reported(self):
        """Assert response status is 208 ALREADY_REPORTED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.ALREADY_REPORTED)

    @then
    def assert_http_im_used(self):
        """Assert response status is 226 IM_USED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.IM_USED)

    @then
    def assert_http_multiple_choices(self):
        """Assert response status is 300 MULTIPLE_CHOICES."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.MULTIPLE_CHOICES)

    @then
    def assert_http_moved_permanently(self):
        """Assert response status is 301 MOVED_PERMANENTLY."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.MOVED_PERMANENTLY)

    @then
    def assert_http_found(self):
        """Assert response status is 302 FOUND."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.FOUND)

    @then
    def assert_http_see_other(self):
        """Assert response status is 303 SEE_OTHER."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.SEE_OTHER)

    @then
    def assert_http_not_modified(self):
        """Assert response status is 304 NOT_MODIFIED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.NOT_MODIFIED)

    @then
    def assert_http_use_proxy(self):
        """Assert response status is 305 USE_PROXY."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.USE_PROXY)

    @then
    def assert_http_temporary_redirect(self):
        """Assert response status is 307 TEMPORARY_REDIRECT."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.TEMPORARY_REDIRECT
        )

    @then
    def assert_http_permanent_redirect(self):
        """Assert response status is 308 PERMANENT_REDIRECT."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.PERMANENT_REDIRECT
        )

    @then
    def assert_http_bad_request(self):
        """Assert response status is 400 BAD_REQUEST."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.BAD_REQUEST)

    @then
    def assert_http_unauthorized(self):
        """Assert response status is 401 UNAUTHORIZED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.UNAUTHORIZED)

    @then
    def assert_http_payment_required(self):
        """Assert response status is 402 PAYMENT_REQUIRED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.PAYMENT_REQUIRED)

    @then
    def assert_http_forbidden(self):
        """Assert response status is 403 FORBIDDEN."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.FORBIDDEN)

    @then
    def assert_http_not_found(self):
        """Assert response status is 404 NOT_FOUND."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.NOT_FOUND)

    @then
    def assert_http_method_not_allowed(self):
        """Assert response status is 405 METHOD_NOT_ALLOWED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.METHOD_NOT_ALLOWED
        )

    @then
    def assert_http_not_acceptable(self):
        """Assert response status is 406 NOT_ACCEPTABLE."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.NOT_ACCEPTABLE)

    @then
    def assert_http_proxy_authentication_required(self):
        """Assert response status is 407 PROXY_AUTHENTICATION_REQUIRED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.PROXY_AUTHENTICATION_REQUIRED
        )

    @then
    def assert_http_request_timeout(self):
        """Assert response status is 408 REQUEST_TIMEOUT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.REQUEST_TIMEOUT)

    @then
    def assert_http_conflict(self):
        """Assert response status is 409 CONFLICT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.CONFLICT)

    @then
    def assert_http_gone(self):
        """Assert response status is 410 GONE."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.GONE)

    @then
    def assert_http_length_required(self):
        """Assert response status is 411 LENGTH_REQUIRED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.LENGTH_REQUIRED)

    @then
    def assert_http_precondition_failed(self):
        """Assert response status is 412 PRECONDITION_FAILED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.PRECONDITION_FAILED
        )

    @then
    def assert_http_request_entity_too_large(self):
        """Assert response status is 413 REQUEST_ENTITY_TOO_LARGE."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.REQUEST_ENTITY_TOO_LARGE
        )

    @then
    def assert_http_request_uri_too_long(self):
        """Assert response status is 414 REQUEST_URI_TOO_LONG."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.REQUEST_URI_TOO_LONG
        )

    @then
    def assert_http_unsupported_media_type(self):
        """Assert response status is 415 UNSUPPORTED_MEDIA_TYPE."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.UNSUPPORTED_MEDIA_TYPE
        )

    @then
    def assert_http_requested_range_not_satisfiable(self):
        """Assert response status is 416 REQUESTED_RANGE_NOT_SATISFIABLE."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.REQUESTED_RANGE_NOT_SATISFIABLE
        )

    @then
    def assert_http_expectation_failed(self):
        """Assert response status is 417 EXPECTATION_FAILED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.EXPECTATION_FAILED
        )

    @then
    def assert_http_im_a_teapot(self):
        """Assert response status is 418 IM_A_TEAPOT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.IM_A_TEAPOT)

    @then
    def assert_http_misdirected_request(self):
        """Assert response status is 421 MISDIRECTED_REQUEST."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.MISDIRECTED_REQUEST
        )

    @then
    def assert_http_unprocessable_entity(self):
        """Assert response status is 422 UNPROCESSABLE_ENTITY."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.UNPROCESSABLE_ENTITY
        )

    @then
    def assert_http_locked(self):
        """Assert response status is 423 LOCKED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.LOCKED)

    @then
    def assert_http_failed_dependency(self):
        """Assert response status is 424 FAILED_DEPENDENCY."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.FAILED_DEPENDENCY)

    @then
    def assert_http_too_early(self):
        """Assert response status is 425 TOO_EARLY."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.TOO_EARLY)

    @then
    def assert_http_upgrade_required(self):
        """Assert response status is 426 UPGRADE_REQUIRED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.UPGRADE_REQUIRED)

    @then
    def assert_http_precondition_required(self):
        """Assert response status is 428 PRECONDITION_REQUIRED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.PRECONDITION_REQUIRED
        )

    @then
    def assert_http_too_many_requests(self):
        """Assert response status is 429 TOO_MANY_REQUESTS."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.TOO_MANY_REQUESTS)

    @then
    def assert_http_request_header_fields_too_large(self):
        """Assert response status is 431 REQUEST_HEADER_FIELDS_TOO_LARGE."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.REQUEST_HEADER_FIELDS_TOO_LARGE
        )

    @then
    def assert_http_unavailable_for_legal_reasons(self):
        """Assert response status is 451 UNAVAILABLE_FOR_LEGAL_REASONS."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.UNAVAILABLE_FOR_LEGAL_REASONS
        )

    @then
    def assert_http_internal_server_error(self):
        """Assert response status is 500 INTERNAL_SERVER_ERROR."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.INTERNAL_SERVER_ERROR
        )

    @then
    def assert_http_not_implemented(self):
        """Assert response status is 501 NOT_IMPLEMENTED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.NOT_IMPLEMENTED)

    @then
    def assert_http_bad_gateway(self):
        """Assert response status is 502 BAD_GATEWAY."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.BAD_GATEWAY)

    @then
    def assert_http_service_unavailable(self):
        """Assert response status is 503 SERVICE_UNAVAILABLE."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.SERVICE_UNAVAILABLE
        )

    @then
    def assert_http_gateway_timeout(self):
        """Assert response status is 504 GATEWAY_TIMEOUT."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.GATEWAY_TIMEOUT)

    @then
    def assert_http_http_version_not_supported(self):
        """Assert response status is 505 HTTP_VERSION_NOT_SUPPORTED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.HTTP_VERSION_NOT_SUPPORTED
        )

    @then
    def assert_http_variant_also_negotiates(self):
        """Assert response status is 506 VARIANT_ALSO_NEGOTIATES."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.VARIANT_ALSO_NEGOTIATES
        )

    @then
    def assert_http_insufficient_storage(self):
        """Assert response status is 507 INSUFFICIENT_STORAGE."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.INSUFFICIENT_STORAGE
        )

    @then
    def assert_http_loop_detected(self):
        """Assert response status is 508 LOOP_DETECTED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.LOOP_DETECTED)

    @then
    def assert_http_not_extended(self):
        """Assert response status is 510 NOT_EXTENDED."""
        AssertThat(self.response.status_code).IsEqualTo(HTTP.NOT_EXTENDED)

    @then
    def assert_http_network_authentication_required(self):
        """Assert response status is 511 NETWORK_AUTHENTICATION_REQUIRED."""
        AssertThat(self.response.status_code).IsEqualTo(
            HTTP.NETWORK_AUTHENTICATION_REQUIRED
        )
