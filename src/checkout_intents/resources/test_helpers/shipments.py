# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.test_helpers.shipment_advance_response import ShipmentAdvanceResponse

__all__ = ["ShipmentsResource", "AsyncShipmentsResource"]


class ShipmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShipmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return ShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShipmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return ShipmentsResourceWithStreamingResponse(self)

    def advance(
        self,
        checkout_intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ShipmentAdvanceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkout_intent_id:
            raise ValueError(f"Expected a non-empty value for `checkout_intent_id` but received {checkout_intent_id!r}")
        return self._post(
            path_template(
                "/api/v1/test-helpers/checkout-intents/{checkout_intent_id}/shipments/advance",
                checkout_intent_id=checkout_intent_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ShipmentAdvanceResponse,
        )


class AsyncShipmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShipmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShipmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncShipmentsResourceWithStreamingResponse(self)

    async def advance(
        self,
        checkout_intent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ShipmentAdvanceResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not checkout_intent_id:
            raise ValueError(f"Expected a non-empty value for `checkout_intent_id` but received {checkout_intent_id!r}")
        return await self._post(
            path_template(
                "/api/v1/test-helpers/checkout-intents/{checkout_intent_id}/shipments/advance",
                checkout_intent_id=checkout_intent_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ShipmentAdvanceResponse,
        )


class ShipmentsResourceWithRawResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.advance = to_raw_response_wrapper(
            shipments.advance,
        )


class AsyncShipmentsResourceWithRawResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.advance = async_to_raw_response_wrapper(
            shipments.advance,
        )


class ShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.advance = to_streamed_response_wrapper(
            shipments.advance,
        )


class AsyncShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.advance = async_to_streamed_response_wrapper(
            shipments.advance,
        )
