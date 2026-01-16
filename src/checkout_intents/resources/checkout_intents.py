# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import logging
from typing import Any, List, Union, TypeVar, Callable, Iterable, cast
from typing_extensions import Literal, TypeGuard

import httpx

from ..types import (
    checkout_intent_list_params,
    checkout_intent_create_params,
    checkout_intent_confirm_params,
    checkout_intent_purchase_params,
    checkout_intent_add_payment_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPagination, AsyncCursorPagination
from .._exceptions import PollTimeoutError
from .._base_client import AsyncPaginator, make_request_options
from ..types.buyer_param import BuyerParam
from ..types.checkout_intent import (
    CheckoutIntent,
    FailedCheckoutIntent,
    CompletedCheckoutIntent,
    AwaitingConfirmationCheckoutIntent,
)
from ..types.payment_method_param import PaymentMethodParam
from ..types.variant_selection_param import VariantSelectionParam

__all__ = ["CheckoutIntentsResource", "AsyncCheckoutIntentsResource"]

T = TypeVar("T", bound=CheckoutIntent)

logger: logging.Logger = logging.getLogger(__name__)


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
        quantity: int,
        constraints: checkout_intent_create_params.Constraints | Omit = omit,
        promo_codes: SequenceNotStr[str] | Omit = omit,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutIntent:
        """
        Create a checkout intent with the given request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                        "constraints": constraints,
                        "promo_codes": promo_codes,
                        "variant_selections": variant_selections,
                    },
                    checkout_intent_create_params.CheckoutIntentCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: float | Omit = omit,
        state: List[Literal["retrieving_offer", "awaiting_confirmation", "placing_order", "completed", "failed"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[CheckoutIntent]:
        """
        Retrieve a paginated list of checkout intents

        Enables developers to query checkout intents associated with their account, with
        filters and cursor-based pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/checkout-intents",
            page=SyncCursorPagination[CheckoutIntent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "state": state,
                    },
                    checkout_intent_list_params.CheckoutIntentListParams,
                ),
            ),
            model=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
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
        idempotency_key: str | None = None,
    ) -> CheckoutIntent:
        """
        Add payment details to a checkout intent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
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
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def purchase(
        self,
        *,
        buyer: BuyerParam,
        product_url: str,
        quantity: int,
        constraints: checkout_intent_purchase_params.Constraints | Omit = omit,
        promo_codes: SequenceNotStr[str] | Omit = omit,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        payment_method: PaymentMethodParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutIntent:
        """
        Create a checkout intent and immediately trigger the purchase workflow.
   
        This is a "fire-and-forget" endpoint that combines create + confirm in one step.
        The workflow handles offer retrieval, payment authorization, and order placement
        asynchronously. Poll the GET endpoint to check status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return cast(
            CheckoutIntent,
            self._post(
                f"/api/v1/checkout-intents/purchase",
                body=maybe_transform(
                    {
                        "buyer": buyer,
                        "payment_method": payment_method,
                        "product_url": product_url,
                        "quantity": quantity,
                        "constraints": constraints,
                        "promo_codes": promo_codes,
                        "variant_selections": variant_selections,
                    },
                    checkout_intent_purchase_params.CheckoutIntentPurchaseParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def _poll_until(
        self,
        id: str,
        condition: Callable[[CheckoutIntent], TypeGuard[T]],
        *,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> T:
        """
        A helper to poll a checkout intent until a specific condition is met.

        Args:
            id: The checkout intent ID to poll
            condition: A callable that returns True when the desired state is reached
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once the condition is met

        Raises:
            CheckoutIntentsError: If the maximum number of attempts is reached without the condition being met
        """
        if max_attempts < 1:
            logger.warning(
                "[Checkout Intents SDK] Invalid max_attempts value: %s. max_attempts must be >= 1. "
                "Defaulting to 1 to ensure at least one polling attempt.",
                max_attempts,
            )
            max_attempts = 1

        attempts = 0

        # Build headers for polling
        poll_headers: dict[str, str] = {
            "X-Stainless-Poll-Helper": "true",
            "X-Stainless-Custom-Poll-Interval": str(int(poll_interval * 1000)),
        }
        if extra_headers:
            for k, v in extra_headers.items():
                if not isinstance(v, Omit):
                    poll_headers[k] = v  # type: ignore[assignment]

        while attempts < max_attempts:
            # Use with_raw_response to access response headers
            response = self.with_raw_response.retrieve(
                id,
                extra_headers=poll_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            intent = response.parse()

            # Check if condition is met
            if condition(intent):
                return intent

            attempts += 1

            # If we've reached max attempts, throw an error
            if attempts >= max_attempts:
                raise PollTimeoutError(
                    intent_id=id,
                    attempts=attempts,
                    poll_interval=poll_interval,
                    max_attempts=max_attempts,
                )

            # Check if server suggests a polling interval
            sleep_interval = poll_interval
            header_interval = response.headers.get("retry-after-ms")
            if header_interval:
                try:
                    header_interval_ms = int(header_interval)
                    sleep_interval = header_interval_ms / 1000.0
                except ValueError:
                    pass  # Ignore invalid header values

            # Sleep before next poll
            self._sleep(sleep_interval)

        # This should never be reached due to the throw above, but TypeScript needs it
        raise PollTimeoutError(
            intent_id=id,
            attempts=attempts,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
        )

    def poll_until_completed(
        self,
        id: str,
        *,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[CompletedCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to poll a checkout intent until it reaches a completed state
        (completed or failed).

        Args:
            id: The checkout intent ID to poll
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches completed or failed state

        Example:
            ```python
            checkout_intent = client.checkout_intents.poll_until_completed("id")
            if checkout_intent.state == "completed":
                print("Order placed successfully!")
            elif checkout_intent.state == "failed":
                print("Order failed:", checkout_intent.failure_reason)
            ```
        """

        def is_completed(
            intent: CheckoutIntent,
        ) -> TypeGuard[Union[CompletedCheckoutIntent, FailedCheckoutIntent]]:
            return intent.state in ("completed", "failed")

        return self._poll_until(
            id,
            is_completed,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def poll_until_awaiting_confirmation(
        self,
        id: str,
        *,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to poll a checkout intent until it's ready for confirmation
        (awaiting_confirmation state) or has failed. This is typically used after
        creating a checkout intent to wait for the offer to be retrieved from the merchant.

        The intent can reach awaiting_confirmation (success - ready to confirm) or failed
        (offer retrieval failed). Always check the state after polling.

        Args:
            id: The checkout intent ID to poll
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches awaiting_confirmation or failed state

        Example:
            ```python
            intent = client.checkout_intents.poll_until_awaiting_confirmation("id")

            if intent.state == "awaiting_confirmation":
                # Review the offer before confirming
                print("Total:", intent.offer.cost.total)
            elif intent.state == "failed":
                # Handle failure (e.g., offer retrieval failed, product out of stock)
                print("Failed:", intent.failure_reason)
            ```
        """

        def is_awaiting_confirmation(
            intent: CheckoutIntent,
        ) -> TypeGuard[Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]]:
            return intent.state in ("awaiting_confirmation", "failed")

        return self._poll_until(
            id,
            is_awaiting_confirmation,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def create_and_poll(
        self,
        *,
        buyer: BuyerParam,
        product_url: str,
        quantity: int,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to create a checkout intent and poll until it's ready for confirmation.
        This follows the Rye documented flow: create → poll until awaiting_confirmation.

        After this method completes, you should review the offer (pricing, shipping, taxes)
        with the user before calling confirm().

        Args:
            buyer: Buyer information
            product_url: URL of the product to purchase
            quantity: Quantity of the product
            variant_selections: Product variant selections (optional)
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches awaiting_confirmation or failed state

        Example:
            ```python
            # Phase 1: Create and wait for offer
            intent = client.checkout_intents.create_and_poll(
                buyer={
                    "address1": "123 Main St",
                    "city": "New York",
                    "country": "US",
                    "email": "john.doe@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "phone": "1234567890",
                    "postal_code": "10001",
                    "province": "NY",
                },
                product_url="https://example.com/product",
                quantity=1,
            )

            # Review the offer with the user
            print("Total:", intent.offer.cost.total)

            # Phase 2: Confirm with payment
            completed = client.checkout_intents.confirm_and_poll(
                intent.id, payment_method={"type": "stripe_token", "stripe_token": "tok_visa"}
            )
            ```
        """
        intent = self.create(
            buyer=buyer,
            product_url=product_url,
            quantity=quantity,
            variant_selections=variant_selections,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self.poll_until_awaiting_confirmation(
            intent.id,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    def confirm_and_poll(
        self,
        id: str,
        *,
        payment_method: PaymentMethodParam,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[CompletedCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to confirm a checkout intent and poll until it reaches a completed state
        (completed or failed).

        Args:
            id: The checkout intent ID to confirm
            payment_method: Payment method information
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches completed or failed state

        Example:
            ```python
            checkout_intent = client.checkout_intents.confirm_and_poll(
                "id",
                payment_method={
                    "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                    "type": "stripe_token",
                },
            )

            if checkout_intent.state == "completed":
                print("Order placed successfully!")
            elif checkout_intent.state == "failed":
                print("Order failed:", checkout_intent.failure_reason)
            ```
        """
        intent = self.confirm(
            id,
            payment_method=payment_method,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return self.poll_until_completed(
            intent.id,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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
        quantity: int,
        constraints: checkout_intent_create_params.Constraints | Omit = omit,
        promo_codes: SequenceNotStr[str] | Omit = omit,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutIntent:
        """
        Create a checkout intent with the given request body.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                        "constraints": constraints,
                        "promo_codes": promo_codes,
                        "variant_selections": variant_selections,
                    },
                    checkout_intent_create_params.CheckoutIntentCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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

    def list(
        self,
        *,
        id: SequenceNotStr[str] | Omit = omit,
        after: str | Omit = omit,
        before: str | Omit = omit,
        limit: float | Omit = omit,
        state: List[Literal["retrieving_offer", "awaiting_confirmation", "placing_order", "completed", "failed"]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CheckoutIntent, AsyncCursorPagination[CheckoutIntent]]:
        """
        Retrieve a paginated list of checkout intents

        Enables developers to query checkout intents associated with their account, with
        filters and cursor-based pagination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/checkout-intents",
            page=AsyncCursorPagination[CheckoutIntent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "after": after,
                        "before": before,
                        "limit": limit,
                        "state": state,
                    },
                    checkout_intent_list_params.CheckoutIntentListParams,
                ),
            ),
            model=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
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
        idempotency_key: str | None = None,
    ) -> CheckoutIntent:
        """
        Add payment details to a checkout intent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
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
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
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
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
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
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def purchase(
        self,
        *,
        buyer: BuyerParam,
        product_url: str,
        quantity: int,
        constraints: checkout_intent_purchase_params.Constraints | Omit = omit,
        promo_codes: SequenceNotStr[str] | Omit = omit,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        payment_method: PaymentMethodParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> CheckoutIntent:
        """
        Create a checkout intent and immediately trigger the purchase workflow.
   
        This is a "fire-and-forget" endpoint that combines create + confirm in one step.
        The workflow handles offer retrieval, payment authorization, and order placement
        asynchronously. Poll the GET endpoint to check status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return cast(
            CheckoutIntent,
            await self._post(
                f"/api/v1/checkout-intents/purchase",
                body=await async_maybe_transform(
                    {
                        "buyer": buyer,
                        "payment_method": payment_method,
                        "product_url": product_url,
                        "quantity": quantity,
                        "constraints": constraints,
                        "promo_codes": promo_codes,
                        "variant_selections": variant_selections,
                    },
                    checkout_intent_purchase_params.CheckoutIntentPurchaseParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(Any, CheckoutIntent),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def _poll_until(
        self,
        id: str,
        condition: Callable[[CheckoutIntent], TypeGuard[T]],
        *,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> T:
        """
        A helper to poll a checkout intent until a specific condition is met.

        Args:
            id: The checkout intent ID to poll
            condition: A callable that returns True when the desired state is reached
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once the condition is met

        Raises:
            CheckoutIntentsError: If the maximum number of attempts is reached without the condition being met
        """
        if max_attempts < 1:
            logger.warning(
                "[Checkout Intents SDK] Invalid max_attempts value: %s. max_attempts must be >= 1. "
                "Defaulting to 1 to ensure at least one polling attempt.",
                max_attempts,
            )
            max_attempts = 1

        attempts = 0

        # Build headers for polling
        poll_headers: dict[str, str] = {
            "X-Stainless-Poll-Helper": "true",
            "X-Stainless-Custom-Poll-Interval": str(int(poll_interval * 1000)),
        }
        if extra_headers:
            for k, v in extra_headers.items():
                if not isinstance(v, Omit):
                    poll_headers[k] = v  # type: ignore[assignment]

        while attempts < max_attempts:
            # Use with_raw_response to access response headers
            response = await self.with_raw_response.retrieve(
                id,
                extra_headers=poll_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            )

            intent = await response.parse()

            # Check if condition is met
            if condition(intent):
                return intent

            attempts += 1

            # If we've reached max attempts, throw an error
            if attempts >= max_attempts:
                raise PollTimeoutError(
                    intent_id=id,
                    attempts=attempts,
                    poll_interval=poll_interval,
                    max_attempts=max_attempts,
                )

            # Check if server suggests a polling interval
            sleep_interval = poll_interval
            header_interval = response.headers.get("retry-after-ms")
            if header_interval:
                try:
                    header_interval_ms = int(header_interval)
                    sleep_interval = header_interval_ms / 1000.0
                except ValueError:
                    pass  # Ignore invalid header values

            # Sleep before next poll
            await self._sleep(sleep_interval)

        # This should never be reached due to the throw above, but TypeScript needs it
        raise PollTimeoutError(
            intent_id=id,
            attempts=attempts,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
        )

    async def poll_until_completed(
        self,
        id: str,
        *,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[CompletedCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to poll a checkout intent until it reaches a completed state
        (completed or failed).

        Args:
            id: The checkout intent ID to poll
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches completed or failed state

        Example:
            ```python
            checkout_intent = await client.checkout_intents.poll_until_completed("id")
            if checkout_intent.state == "completed":
                print("Order placed successfully!")
            elif checkout_intent.state == "failed":
                print("Order failed:", checkout_intent.failure_reason)
            ```
        """

        def is_completed(
            intent: CheckoutIntent,
        ) -> TypeGuard[Union[CompletedCheckoutIntent, FailedCheckoutIntent]]:
            return intent.state in ("completed", "failed")

        return await self._poll_until(
            id,
            is_completed,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def poll_until_awaiting_confirmation(
        self,
        id: str,
        *,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to poll a checkout intent until it's ready for confirmation
        (awaiting_confirmation state) or has failed. This is typically used after
        creating a checkout intent to wait for the offer to be retrieved from the merchant.

        The intent can reach awaiting_confirmation (success - ready to confirm) or failed
        (offer retrieval failed). Always check the state after polling.

        Args:
            id: The checkout intent ID to poll
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches awaiting_confirmation or failed state

        Example:
            ```python
            intent = await client.checkout_intents.poll_until_awaiting_confirmation("id")

            if intent.state == "awaiting_confirmation":
                # Review the offer before confirming
                print("Total:", intent.offer.cost.total)
            elif intent.state == "failed":
                # Handle failure (e.g., offer retrieval failed, product out of stock)
                print("Failed:", intent.failure_reason)
            ```
        """

        def is_awaiting_confirmation(
            intent: CheckoutIntent,
        ) -> TypeGuard[Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]]:
            return intent.state in ("awaiting_confirmation", "failed")

        return await self._poll_until(
            id,
            is_awaiting_confirmation,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def create_and_poll(
        self,
        *,
        buyer: BuyerParam,
        product_url: str,
        quantity: int,
        variant_selections: Iterable[VariantSelectionParam] | Omit = omit,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to create a checkout intent and poll until it's ready for confirmation.
        This follows the Rye documented flow: create → poll until awaiting_confirmation.

        After this method completes, you should review the offer (pricing, shipping, taxes)
        with the user before calling confirm().

        Args:
            buyer: Buyer information
            product_url: URL of the product to purchase
            quantity: Quantity of the product
            variant_selections: Product variant selections (optional)
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches awaiting_confirmation or failed state

        Example:
            ```python
            # Phase 1: Create and wait for offer
            intent = await client.checkout_intents.create_and_poll(
                buyer={
                    "address1": "123 Main St",
                    "city": "New York",
                    "country": "US",
                    "email": "john.doe@example.com",
                    "first_name": "John",
                    "last_name": "Doe",
                    "phone": "1234567890",
                    "postal_code": "10001",
                    "province": "NY",
                },
                product_url="https://example.com/product",
                quantity=1,
            )

            # Review the offer with the user
            print("Total:", intent.offer.cost.total)

            # Phase 2: Confirm with payment
            completed = await client.checkout_intents.confirm_and_poll(
                intent.id, payment_method={"type": "stripe_token", "stripe_token": "tok_visa"}
            )
            ```
        """
        intent = await self.create(
            buyer=buyer,
            product_url=product_url,
            quantity=quantity,
            variant_selections=variant_selections,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self.poll_until_awaiting_confirmation(
            intent.id,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )

    async def confirm_and_poll(
        self,
        id: str,
        *,
        payment_method: PaymentMethodParam,
        poll_interval: float = 5.0,
        max_attempts: int = 120,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Union[CompletedCheckoutIntent, FailedCheckoutIntent]:
        """
        A helper to confirm a checkout intent and poll until it reaches a completed state
        (completed or failed).

        Args:
            id: The checkout intent ID to confirm
            payment_method: Payment method information
            poll_interval: The interval in seconds between polling attempts (default: 5.0)
            max_attempts: The maximum number of polling attempts before timing out (default: 120)
            extra_headers: Send extra headers
            extra_query: Add additional query parameters to the request
            extra_body: Add additional JSON properties to the request
            timeout: Override the client-level default timeout for this request, in seconds

        Returns:
            The checkout intent once it reaches completed or failed state

        Example:
            ```python
            checkout_intent = await client.checkout_intents.confirm_and_poll(
                "id",
                payment_method={
                    "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                    "type": "stripe_token",
                },
            )

            if checkout_intent.state == "completed":
                print("Order placed successfully!")
            elif checkout_intent.state == "failed":
                print("Order failed:", checkout_intent.failure_reason)
            ```
        """
        intent = await self.confirm(
            id,
            payment_method=payment_method,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return await self.poll_until_completed(
            intent.id,
            poll_interval=poll_interval,
            max_attempts=max_attempts,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
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
        self.list = to_raw_response_wrapper(
            checkout_intents.list,
        )
        self.add_payment = to_raw_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = to_raw_response_wrapper(
            checkout_intents.confirm,
        )
        self.purchase = to_raw_response_wrapper(
            checkout_intents.purchase,
        )
        self.poll_until_completed = to_raw_response_wrapper(
            checkout_intents.poll_until_completed,
        )
        self.poll_until_awaiting_confirmation = to_raw_response_wrapper(
            checkout_intents.poll_until_awaiting_confirmation,
        )
        self.create_and_poll = to_raw_response_wrapper(
            checkout_intents.create_and_poll,
        )
        self.confirm_and_poll = to_raw_response_wrapper(
            checkout_intents.confirm_and_poll,
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
        self.list = async_to_raw_response_wrapper(
            checkout_intents.list,
        )
        self.add_payment = async_to_raw_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = async_to_raw_response_wrapper(
            checkout_intents.confirm,
        )
        self.purchase = async_to_raw_response_wrapper(
            checkout_intents.purchase,
        )
        self.poll_until_completed = async_to_raw_response_wrapper(
            checkout_intents.poll_until_completed,
        )
        self.poll_until_awaiting_confirmation = async_to_raw_response_wrapper(
            checkout_intents.poll_until_awaiting_confirmation,
        )
        self.create_and_poll = async_to_raw_response_wrapper(
            checkout_intents.create_and_poll,
        )
        self.confirm_and_poll = async_to_raw_response_wrapper(
            checkout_intents.confirm_and_poll,
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
        self.list = to_streamed_response_wrapper(
            checkout_intents.list,
        )
        self.add_payment = to_streamed_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = to_streamed_response_wrapper(
            checkout_intents.confirm,
        )
        self.purchase = to_streamed_response_wrapper(
            checkout_intents.purchase,
        )
        self.poll_until_completed = to_streamed_response_wrapper(
            checkout_intents.poll_until_completed,
        )
        self.poll_until_awaiting_confirmation = to_streamed_response_wrapper(
            checkout_intents.poll_until_awaiting_confirmation,
        )
        self.create_and_poll = to_streamed_response_wrapper(
            checkout_intents.create_and_poll,
        )
        self.confirm_and_poll = to_streamed_response_wrapper(
            checkout_intents.confirm_and_poll,
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
        self.list = async_to_streamed_response_wrapper(
            checkout_intents.list,
        )
        self.add_payment = async_to_streamed_response_wrapper(
            checkout_intents.add_payment,
        )
        self.confirm = async_to_streamed_response_wrapper(
            checkout_intents.confirm,
        )
        self.purchase = async_to_streamed_response_wrapper(
            checkout_intents.purchase,
        )
        self.poll_until_completed = async_to_streamed_response_wrapper(
            checkout_intents.poll_until_completed,
        )
        self.poll_until_awaiting_confirmation = async_to_streamed_response_wrapper(
            checkout_intents.poll_until_awaiting_confirmation,
        )
        self.create_and_poll = async_to_streamed_response_wrapper(
            checkout_intents.create_and_poll,
        )
        self.confirm_and_poll = async_to_streamed_response_wrapper(
            checkout_intents.confirm_and_poll,
        )
