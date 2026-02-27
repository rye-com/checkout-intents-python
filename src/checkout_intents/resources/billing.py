# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import billing_list_transactions_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPagination, AsyncCursorPagination
from .._base_client import AsyncPaginator, make_request_options
from ..types.billing_get_balance_response import BillingGetBalanceResponse
from ..types.billing_list_transactions_response import BillingListTransactionsResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def get_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetBalanceResponse:
        """Get current drawdown balance for the authenticated developer"""
        return self._get(
            "/api/v1/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetBalanceResponse,
        )

    def list_transactions(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[BillingListTransactionsResponse]:
        """
        List drawdown balance transactions for the authenticated developer

        Args:
          after: Cursor for forward pagination (transaction ID to start after)

          before: Cursor for backward pagination (transaction ID to end before)

          limit: Maximum number of transactions to return (default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/billing/transactions",
            page=SyncCursorPagination[BillingListTransactionsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    billing_list_transactions_params.BillingListTransactionsParams,
                ),
            ),
            model=BillingListTransactionsResponse,
        )


class AsyncBillingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def get_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetBalanceResponse:
        """Get current drawdown balance for the authenticated developer"""
        return await self._get(
            "/api/v1/billing/balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetBalanceResponse,
        )

    def list_transactions(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BillingListTransactionsResponse, AsyncCursorPagination[BillingListTransactionsResponse]]:
        """
        List drawdown balance transactions for the authenticated developer

        Args:
          after: Cursor for forward pagination (transaction ID to start after)

          before: Cursor for backward pagination (transaction ID to end before)

          limit: Maximum number of transactions to return (default 20)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/billing/transactions",
            page=AsyncCursorPagination[BillingListTransactionsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "limit": limit,
                    },
                    billing_list_transactions_params.BillingListTransactionsParams,
                ),
            ),
            model=BillingListTransactionsResponse,
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_balance = to_raw_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = to_raw_response_wrapper(
            billing.list_transactions,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_balance = async_to_raw_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            billing.list_transactions,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_balance = to_streamed_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = to_streamed_response_wrapper(
            billing.list_transactions,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_balance = async_to_streamed_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            billing.list_transactions,
        )
