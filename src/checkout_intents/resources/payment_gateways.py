# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import PaymentGateway
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.payment_gateway import PaymentGateway
from ..types.payment_gateway_session import PaymentGatewaySession

__all__ = ["PaymentGatewaysResource", "AsyncPaymentGatewaysResource"]


class PaymentGatewaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return PaymentGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return PaymentGatewaysResourceWithStreamingResponse(self)

    def create_session(
        self,
        gateway: PaymentGateway,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentGatewaySession:
        """
        Create a payment gateway session for client-side card tokenization.

        Returns short-lived credentials scoped to the authenticated developer. Use the
        credentials with the corresponding gateway's client-side SDK to tokenize a card.
        Tokens created this way are locked to the developer's container and cannot be
        used by other developers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not gateway:
            raise ValueError(f"Expected a non-empty value for `gateway` but received {gateway!r}")
        return self._post(
            path_template("/api/v1/payment-gateways/{gateway}/session", gateway=gateway),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentGatewaySession,
        )


class AsyncPaymentGatewaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncPaymentGatewaysResourceWithStreamingResponse(self)

    async def create_session(
        self,
        gateway: PaymentGateway,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> PaymentGatewaySession:
        """
        Create a payment gateway session for client-side card tokenization.

        Returns short-lived credentials scoped to the authenticated developer. Use the
        credentials with the corresponding gateway's client-side SDK to tokenize a card.
        Tokens created this way are locked to the developer's container and cannot be
        used by other developers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not gateway:
            raise ValueError(f"Expected a non-empty value for `gateway` but received {gateway!r}")
        return await self._post(
            path_template("/api/v1/payment-gateways/{gateway}/session", gateway=gateway),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=PaymentGatewaySession,
        )


class PaymentGatewaysResourceWithRawResponse:
    def __init__(self, payment_gateways: PaymentGatewaysResource) -> None:
        self._payment_gateways = payment_gateways

        self.create_session = to_raw_response_wrapper(
            payment_gateways.create_session,
        )


class AsyncPaymentGatewaysResourceWithRawResponse:
    def __init__(self, payment_gateways: AsyncPaymentGatewaysResource) -> None:
        self._payment_gateways = payment_gateways

        self.create_session = async_to_raw_response_wrapper(
            payment_gateways.create_session,
        )


class PaymentGatewaysResourceWithStreamingResponse:
    def __init__(self, payment_gateways: PaymentGatewaysResource) -> None:
        self._payment_gateways = payment_gateways

        self.create_session = to_streamed_response_wrapper(
            payment_gateways.create_session,
        )


class AsyncPaymentGatewaysResourceWithStreamingResponse:
    def __init__(self, payment_gateways: AsyncPaymentGatewaysResource) -> None:
        self._payment_gateways = payment_gateways

        self.create_session = async_to_streamed_response_wrapper(
            payment_gateways.create_session,
        )
