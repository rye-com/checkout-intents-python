# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import billing_list_transactions_params, billing_create_topup_invoice_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
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
from ..types.billing_create_topup_invoice_response import BillingCreateTopupInvoiceResponse

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

    def cancel_topup_invoice(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Cancel/void an unpaid top-up invoice.

        Only invoices in open state can be
        cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/billing/drawdown/topup/{invoice_id}", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def create_topup_invoice(
        self,
        *,
        amount_subunits: int,
        charge_automatically: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingCreateTopupInvoiceResponse:
        """Request an on-demand top-up invoice..

        Requires drawdown billing to be enabled.
        Only one unpaid top-up invoice is allowed at a time.

        Args:
          amount_subunits: Amount in smallest currency unit (e.g. cents).

          charge_automatically: Override whether to automatically charge the invoice. Defaults to the
              developer's drawdown config value if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/api/v1/billing/drawdown/topup",
            body=maybe_transform(
                {
                    "amount_subunits": amount_subunits,
                    "charge_automatically": charge_automatically,
                },
                billing_create_topup_invoice_params.BillingCreateTopupInvoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingCreateTopupInvoiceResponse,
        )

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

    async def cancel_topup_invoice(
        self,
        invoice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> None:
        """Cancel/void an unpaid top-up invoice.

        Only invoices in open state can be
        cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/billing/drawdown/topup/{invoice_id}", invoice_id=invoice_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def create_topup_invoice(
        self,
        *,
        amount_subunits: int,
        charge_automatically: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> BillingCreateTopupInvoiceResponse:
        """Request an on-demand top-up invoice..

        Requires drawdown billing to be enabled.
        Only one unpaid top-up invoice is allowed at a time.

        Args:
          amount_subunits: Amount in smallest currency unit (e.g. cents).

          charge_automatically: Override whether to automatically charge the invoice. Defaults to the
              developer's drawdown config value if not specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/api/v1/billing/drawdown/topup",
            body=await async_maybe_transform(
                {
                    "amount_subunits": amount_subunits,
                    "charge_automatically": charge_automatically,
                },
                billing_create_topup_invoice_params.BillingCreateTopupInvoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BillingCreateTopupInvoiceResponse,
        )

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

        self.cancel_topup_invoice = to_raw_response_wrapper(
            billing.cancel_topup_invoice,
        )
        self.create_topup_invoice = to_raw_response_wrapper(
            billing.create_topup_invoice,
        )
        self.get_balance = to_raw_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = to_raw_response_wrapper(
            billing.list_transactions,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.cancel_topup_invoice = async_to_raw_response_wrapper(
            billing.cancel_topup_invoice,
        )
        self.create_topup_invoice = async_to_raw_response_wrapper(
            billing.create_topup_invoice,
        )
        self.get_balance = async_to_raw_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            billing.list_transactions,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.cancel_topup_invoice = to_streamed_response_wrapper(
            billing.cancel_topup_invoice,
        )
        self.create_topup_invoice = to_streamed_response_wrapper(
            billing.create_topup_invoice,
        )
        self.get_balance = to_streamed_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = to_streamed_response_wrapper(
            billing.list_transactions,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.cancel_topup_invoice = async_to_streamed_response_wrapper(
            billing.cancel_topup_invoice,
        )
        self.create_topup_invoice = async_to_streamed_response_wrapper(
            billing.create_topup_invoice,
        )
        self.get_balance = async_to_streamed_response_wrapper(
            billing.get_balance,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            billing.list_transactions,
        )
