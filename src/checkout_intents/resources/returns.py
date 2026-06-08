# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import ReturnReason, return_create_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.return_ import Return
from ..types.return_reason import ReturnReason

__all__ = ["ReturnsResource", "AsyncReturnsResource"]


class ReturnsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReturnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return ReturnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReturnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return ReturnsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        order_id: str,
        reason: ReturnReason,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """Create a return for a completed order.

        Whole-order returns only — the order's
        line items are enumerated for you. The return is submitted for approval and then
        progresses asynchronously toward the refund; poll the returned return id (or
        listen for webhooks) to follow its state.

        Args:
          order_id: Rye order id (`order_<32 hex>`) of the order being returned.

          reason: Reason for the return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/v1/returns",
            body=maybe_transform(
                {
                    "order_id": order_id,
                    "reason": reason,
                },
                return_create_params.ReturnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )

    def retrieve(
        self,
        return_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Return:
        """Fetch a Return by id.

        Tenancy is scoped to the authenticated developer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return self._get(
            path_template("/api/v1/returns/{return_id}", return_id=return_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Return,
        )


class AsyncReturnsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReturnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReturnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReturnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncReturnsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        order_id: str,
        reason: ReturnReason,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """Create a return for a completed order.

        Whole-order returns only — the order's
        line items are enumerated for you. The return is submitted for approval and then
        progresses asynchronously toward the refund; poll the returned return id (or
        listen for webhooks) to follow its state.

        Args:
          order_id: Rye order id (`order_<32 hex>`) of the order being returned.

          reason: Reason for the return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/v1/returns",
            body=await async_maybe_transform(
                {
                    "order_id": order_id,
                    "reason": reason,
                },
                return_create_params.ReturnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )

    async def retrieve(
        self,
        return_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Return:
        """Fetch a Return by id.

        Tenancy is scoped to the authenticated developer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return await self._get(
            path_template("/api/v1/returns/{return_id}", return_id=return_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Return,
        )


class ReturnsResourceWithRawResponse:
    def __init__(self, returns: ReturnsResource) -> None:
        self._returns = returns

        self.create = to_raw_response_wrapper(
            returns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            returns.retrieve,
        )


class AsyncReturnsResourceWithRawResponse:
    def __init__(self, returns: AsyncReturnsResource) -> None:
        self._returns = returns

        self.create = async_to_raw_response_wrapper(
            returns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            returns.retrieve,
        )


class ReturnsResourceWithStreamingResponse:
    def __init__(self, returns: ReturnsResource) -> None:
        self._returns = returns

        self.create = to_streamed_response_wrapper(
            returns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            returns.retrieve,
        )


class AsyncReturnsResourceWithStreamingResponse:
    def __init__(self, returns: AsyncReturnsResource) -> None:
        self._returns = returns

        self.create = async_to_streamed_response_wrapper(
            returns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            returns.retrieve,
        )
