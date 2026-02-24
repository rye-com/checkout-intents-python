from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Union, TypeVar, Callable
from typing_extensions import TypeGuard

import httpx

from .._types import Body, Omit, Query, Headers, NotGiven, not_given
from .._exceptions import PollTimeoutError
from ..types.checkout_intent import (
    CheckoutIntent,
    FailedCheckoutIntent,
    CompletedCheckoutIntent,
    AwaitingConfirmationCheckoutIntent,
)

if TYPE_CHECKING:
    from ..resources.checkout_intents.checkout_intents import (
        CheckoutIntentsResource,
        AsyncCheckoutIntentsResource,
    )

__all__ = [
    "poll_until",
    "async_poll_until",
    "is_completed",
    "is_awaiting_confirmation",
]

T = TypeVar("T", bound=CheckoutIntent)

logger: logging.Logger = logging.getLogger(__name__)


def is_completed(
    intent: CheckoutIntent,
) -> TypeGuard[Union[CompletedCheckoutIntent, FailedCheckoutIntent]]:
    return intent.state in ("completed", "failed")


def is_awaiting_confirmation(
    intent: CheckoutIntent,
) -> TypeGuard[Union[AwaitingConfirmationCheckoutIntent, FailedCheckoutIntent]]:
    return intent.state in ("awaiting_confirmation", "failed")


def poll_until(
    resource: CheckoutIntentsResource,
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
    Poll a checkout intent until a specific condition is met.

    Args:
        resource: The sync CheckoutIntentsResource to use for polling
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
        PollTimeoutError: If the maximum number of attempts is reached without the condition being met
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
        response = resource.with_raw_response.retrieve(
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
        resource._sleep(sleep_interval)

    # This should never be reached due to the throw above, but TypeScript needs it
    raise PollTimeoutError(
        intent_id=id,
        attempts=attempts,
        poll_interval=poll_interval,
        max_attempts=max_attempts,
    )


async def async_poll_until(
    resource: AsyncCheckoutIntentsResource,
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
    Poll a checkout intent until a specific condition is met (async version).

    Args:
        resource: The async AsyncCheckoutIntentsResource to use for polling
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
        PollTimeoutError: If the maximum number of attempts is reached without the condition being met
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
        response = await resource.with_raw_response.retrieve(
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
        await resource._sleep(sleep_interval)

    # This should never be reached due to the throw above, but TypeScript needs it
    raise PollTimeoutError(
        intent_id=id,
        attempts=attempts,
        poll_interval=poll_interval,
        max_attempts=max_attempts,
    )
