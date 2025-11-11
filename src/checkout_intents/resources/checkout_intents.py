# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Iterable, cast

import httpx

from ..types import (
    checkout_intent_create_params,
    checkout_intent_confirm_params,
    checkout_intent_add_payment_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.buyer_param import BuyerParam
from ..types.checkout_intent import CheckoutIntent
from ..types.payment_method_param import PaymentMethodParam
from ..types.variant_selection_param import VariantSelectionParam

__all__ = ["CheckoutIntentsResource", "AsyncCheckoutIntentsResource"]


class CheckoutIntentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckoutIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return CheckoutIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckoutIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return CheckoutIntentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        buyer: BuyerParam,
        product_url: str,
        quantity: float,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Create a checkout intent with the given request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CheckoutIntent,
            self._post(
                "/api/v1/checkout-intents",
                body=maybe_transform(
                    {
                        "buyer": buyer,
                        "product_url": product_url,
                        "quantity": quantity,
                        "variant_selections": variant_selections,
                    },
                    checkout_intent_create_params.CheckoutIntentCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Retrieve a checkout intent by id

        Returns checkout intent information if the lookup succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            CheckoutIntent,
            self._get(
                f"/api/v1/checkout-intents/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def add_payment(
        self,
        id: str,
        *,
        payment_method: PaymentMethodParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Add payment details to a checkout intent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            CheckoutIntent,
            self._post(
                f"/api/v1/checkout-intents/{id}/payment",
                body=maybe_transform(
                    {"payment_method": payment_method},
                    checkout_intent_add_payment_params.CheckoutIntentAddPaymentParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def confirm(
        self,
        id: str,
        *,
        payment_method: PaymentMethodParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Confirm a checkout intent with provided payment information

        Confirm means we have buyer's name, address and payment info, so we can move
        forward to place the order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            CheckoutIntent,
            self._post(
                f"/api/v1/checkout-intents/{id}/confirm",
                body=maybe_transform(
                    {"payment_method": payment_method}, checkout_intent_confirm_params.CheckoutIntentConfirmParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCheckoutIntentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckoutIntentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCheckoutIntentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckoutIntentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncCheckoutIntentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        buyer: BuyerParam,
        product_url: str,
        quantity: float,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Create a checkout intent with the given request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            CheckoutIntent,
            await self._post(
                "/api/v1/checkout-intents",
                body=await async_maybe_transform(
                    {
                        "buyer": buyer,
                        "product_url": product_url,
                        "quantity": quantity,
                        "variant_selections": variant_selections,
                    },
                    checkout_intent_create_params.CheckoutIntentCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Retrieve a checkout intent by id

        Returns checkout intent information if the lookup succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            CheckoutIntent,
            await self._get(
                f"/api/v1/checkout-intents/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def add_payment(
        self,
        id: str,
        *,
        payment_method: PaymentMethodParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Add payment details to a checkout intent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            CheckoutIntent,
            await self._post(
                f"/api/v1/checkout-intents/{id}/payment",
                body=await async_maybe_transform(
                    {"payment_method": payment_method},
                    checkout_intent_add_payment_params.CheckoutIntentAddPaymentParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def confirm(
        self,
        id: str,
        *,
        payment_method: PaymentMethodParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CheckoutIntent:
        """
        Confirm a checkout intent with provided payment information

        Confirm means we have buyer's name, address and payment info, so we can move
        forward to place the order.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            CheckoutIntent,
            await self._post(
                f"/api/v1/checkout-intents/{id}/confirm",
                body=await async_maybe_transform(
                    {"payment_method": payment_method}, checkout_intent_confirm_params.CheckoutIntentConfirmParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CheckoutIntentsResourceWithRawResponse:
    def __init__(self, checkout_intents: CheckoutIntentsResource) -> None:
        self._checkout_intents = checkout_intents

        self.create = to_raw_response_wrapper(
            checkout_intents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            checkout_intents.retrieve,
        )
        self.add_payment = to_raw_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = to_raw_response_wrapper(
            checkout_intents.confirm,
        )


class AsyncCheckoutIntentsResourceWithRawResponse:
    def __init__(self, checkout_intents: AsyncCheckoutIntentsResource) -> None:
        self._checkout_intents = checkout_intents

        self.create = async_to_raw_response_wrapper(
            checkout_intents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            checkout_intents.retrieve,
        )
        self.add_payment = async_to_raw_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = async_to_raw_response_wrapper(
            checkout_intents.confirm,
        )


class CheckoutIntentsResourceWithStreamingResponse:
    def __init__(self, checkout_intents: CheckoutIntentsResource) -> None:
        self._checkout_intents = checkout_intents

        self.create = to_streamed_response_wrapper(
            checkout_intents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            checkout_intents.retrieve,
        )
        self.add_payment = to_streamed_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = to_streamed_response_wrapper(
            checkout_intents.confirm,
        )


class AsyncCheckoutIntentsResourceWithStreamingResponse:
    def __init__(self, checkout_intents: AsyncCheckoutIntentsResource) -> None:
        self._checkout_intents = checkout_intents

        self.create = async_to_streamed_response_wrapper(
            checkout_intents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            checkout_intents.retrieve,
        )
        self.add_payment = async_to_streamed_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = async_to_streamed_response_wrapper(
            checkout_intents.confirm,
        )
