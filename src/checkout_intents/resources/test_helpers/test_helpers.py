# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .returns import (
    ReturnsResource,
    AsyncReturnsResource,
    ReturnsResourceWithRawResponse,
    AsyncReturnsResourceWithRawResponse,
    ReturnsResourceWithStreamingResponse,
    AsyncReturnsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .shipments import (
    ShipmentsResource,
    AsyncShipmentsResource,
    ShipmentsResourceWithRawResponse,
    AsyncShipmentsResourceWithRawResponse,
    ShipmentsResourceWithStreamingResponse,
    AsyncShipmentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TestHelpersResource", "AsyncTestHelpersResource"]


class TestHelpersResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def returns(self) -> ReturnsResource:
        return ReturnsResource(self._client)

    @cached_property
    def shipments(self) -> ShipmentsResource:
        return ShipmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TestHelpersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return TestHelpersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestHelpersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return TestHelpersResourceWithStreamingResponse(self)


class AsyncTestHelpersResource(AsyncAPIResource):
    @cached_property
    def returns(self) -> AsyncReturnsResource:
        return AsyncReturnsResource(self._client)

    @cached_property
    def shipments(self) -> AsyncShipmentsResource:
        return AsyncShipmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTestHelpersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestHelpersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestHelpersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncTestHelpersResourceWithStreamingResponse(self)


class TestHelpersResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_helpers: TestHelpersResource) -> None:
        self._test_helpers = test_helpers

    @cached_property
    def returns(self) -> ReturnsResourceWithRawResponse:
        return ReturnsResourceWithRawResponse(self._test_helpers.returns)

    @cached_property
    def shipments(self) -> ShipmentsResourceWithRawResponse:
        return ShipmentsResourceWithRawResponse(self._test_helpers.shipments)


class AsyncTestHelpersResourceWithRawResponse:
    def __init__(self, test_helpers: AsyncTestHelpersResource) -> None:
        self._test_helpers = test_helpers

    @cached_property
    def returns(self) -> AsyncReturnsResourceWithRawResponse:
        return AsyncReturnsResourceWithRawResponse(self._test_helpers.returns)

    @cached_property
    def shipments(self) -> AsyncShipmentsResourceWithRawResponse:
        return AsyncShipmentsResourceWithRawResponse(self._test_helpers.shipments)


class TestHelpersResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_helpers: TestHelpersResource) -> None:
        self._test_helpers = test_helpers

    @cached_property
    def returns(self) -> ReturnsResourceWithStreamingResponse:
        return ReturnsResourceWithStreamingResponse(self._test_helpers.returns)

    @cached_property
    def shipments(self) -> ShipmentsResourceWithStreamingResponse:
        return ShipmentsResourceWithStreamingResponse(self._test_helpers.shipments)


class AsyncTestHelpersResourceWithStreamingResponse:
    def __init__(self, test_helpers: AsyncTestHelpersResource) -> None:
        self._test_helpers = test_helpers

    @cached_property
    def returns(self) -> AsyncReturnsResourceWithStreamingResponse:
        return AsyncReturnsResourceWithStreamingResponse(self._test_helpers.returns)

    @cached_property
    def shipments(self) -> AsyncShipmentsResourceWithStreamingResponse:
        return AsyncShipmentsResourceWithStreamingResponse(self._test_helpers.shipments)
