# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...types import ReturnReason
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.return_ import Return
from ...types.test_helpers import (
    return_deny_params,
    return_fail_params,
    return_create_params,
    return_refund_params,
    return_approve_params,
)
from ...types.return_reason import ReturnReason

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
        line_items: Iterable[return_create_params.LineItem] | Omit = omit,
        reason: ReturnReason | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Create a simulated return for an order, then drive it through its lifecycle with
        the approve/deny/refund/fail helpers below.

        Args:
          order_id: Rye order id (`oi_<hex>` / `order_<hex>`) to open the simulated return against.

          line_items: Subset of order line items to return. Defaults to every order item at full
              quantity.

          reason: Defaults to `other` when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/v1/test-helpers/returns",
            body=maybe_transform(
                {
                    "order_id": order_id,
                    "line_items": line_items,
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

    def approve(
        self,
        return_id: str,
        *,
        next_action: Literal["ship_items_to_merchant", "no_action_required"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          next_action: `ship_items_to_merchant` lands the return in `requires_action` with a stub
              shipping label; `no_action_required` lands it directly in `processing`. Defaults
              to `ship_items_to_merchant`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/approve", return_id=return_id),
            body=maybe_transform({"next_action": next_action}, return_approve_params.ReturnApproveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )

    def deny(
        self,
        return_id: str,
        *,
        note: str | Omit = omit,
        reason: Literal["final_sale", "return_period_ended", "other"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          reason: Defaults to `other`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/deny", return_id=return_id),
            body=maybe_transform(
                {
                    "note": note,
                    "reason": reason,
                },
                return_deny_params.ReturnDenyParams,
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

    def fail(
        self,
        return_id: str,
        *,
        note: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/fail", return_id=return_id),
            body=maybe_transform({"note": note}, return_fail_params.ReturnFailParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )

    def refund(
        self,
        return_id: str,
        *,
        cost_bearer: Literal["shopper", "developer", "rye"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          cost_bearer: Defaults to `shopper`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/refund", return_id=return_id),
            body=maybe_transform({"cost_bearer": cost_bearer}, return_refund_params.ReturnRefundParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        line_items: Iterable[return_create_params.LineItem] | Omit = omit,
        reason: ReturnReason | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Create a simulated return for an order, then drive it through its lifecycle with
        the approve/deny/refund/fail helpers below.

        Args:
          order_id: Rye order id (`oi_<hex>` / `order_<hex>`) to open the simulated return against.

          line_items: Subset of order line items to return. Defaults to every order item at full
              quantity.

          reason: Defaults to `other` when omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/v1/test-helpers/returns",
            body=await async_maybe_transform(
                {
                    "order_id": order_id,
                    "line_items": line_items,
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

    async def approve(
        self,
        return_id: str,
        *,
        next_action: Literal["ship_items_to_merchant", "no_action_required"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          next_action: `ship_items_to_merchant` lands the return in `requires_action` with a stub
              shipping label; `no_action_required` lands it directly in `processing`. Defaults
              to `ship_items_to_merchant`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return await self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/approve", return_id=return_id),
            body=await async_maybe_transform({"next_action": next_action}, return_approve_params.ReturnApproveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )

    async def deny(
        self,
        return_id: str,
        *,
        note: str | Omit = omit,
        reason: Literal["final_sale", "return_period_ended", "other"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          reason: Defaults to `other`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return await self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/deny", return_id=return_id),
            body=await async_maybe_transform(
                {
                    "note": note,
                    "reason": reason,
                },
                return_deny_params.ReturnDenyParams,
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

    async def fail(
        self,
        return_id: str,
        *,
        note: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return await self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/fail", return_id=return_id),
            body=await async_maybe_transform({"note": note}, return_fail_params.ReturnFailParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )

    async def refund(
        self,
        return_id: str,
        *,
        cost_bearer: Literal["shopper", "developer", "rye"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> Return:
        """
        Args:
          cost_bearer: Defaults to `shopper`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not return_id:
            raise ValueError(f"Expected a non-empty value for `return_id` but received {return_id!r}")
        return await self._post(
            path_template("/api/v1/test-helpers/returns/{return_id}/refund", return_id=return_id),
            body=await async_maybe_transform({"cost_bearer": cost_bearer}, return_refund_params.ReturnRefundParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Return,
        )


class ReturnsResourceWithRawResponse:
    def __init__(self, returns: ReturnsResource) -> None:
        self._returns = returns

        self.create = to_raw_response_wrapper(
            returns.create,
        )
        self.approve = to_raw_response_wrapper(
            returns.approve,
        )
        self.deny = to_raw_response_wrapper(
            returns.deny,
        )
        self.fail = to_raw_response_wrapper(
            returns.fail,
        )
        self.refund = to_raw_response_wrapper(
            returns.refund,
        )


class AsyncReturnsResourceWithRawResponse:
    def __init__(self, returns: AsyncReturnsResource) -> None:
        self._returns = returns

        self.create = async_to_raw_response_wrapper(
            returns.create,
        )
        self.approve = async_to_raw_response_wrapper(
            returns.approve,
        )
        self.deny = async_to_raw_response_wrapper(
            returns.deny,
        )
        self.fail = async_to_raw_response_wrapper(
            returns.fail,
        )
        self.refund = async_to_raw_response_wrapper(
            returns.refund,
        )


class ReturnsResourceWithStreamingResponse:
    def __init__(self, returns: ReturnsResource) -> None:
        self._returns = returns

        self.create = to_streamed_response_wrapper(
            returns.create,
        )
        self.approve = to_streamed_response_wrapper(
            returns.approve,
        )
        self.deny = to_streamed_response_wrapper(
            returns.deny,
        )
        self.fail = to_streamed_response_wrapper(
            returns.fail,
        )
        self.refund = to_streamed_response_wrapper(
            returns.refund,
        )


class AsyncReturnsResourceWithStreamingResponse:
    def __init__(self, returns: AsyncReturnsResource) -> None:
        self._returns = returns

        self.create = async_to_streamed_response_wrapper(
            returns.create,
        )
        self.approve = async_to_streamed_response_wrapper(
            returns.approve,
        )
        self.deny = async_to_streamed_response_wrapper(
            returns.deny,
        )
        self.fail = async_to_streamed_response_wrapper(
            returns.fail,
        )
        self.refund = async_to_streamed_response_wrapper(
            returns.refund,
        )
