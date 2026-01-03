# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .checkout_sessions import (
    CheckoutSessionsResource,
    AsyncCheckoutSessionsResource,
    CheckoutSessionsResourceWithRawResponse,
    AsyncCheckoutSessionsResourceWithRawResponse,
    CheckoutSessionsResourceWithStreamingResponse,
    AsyncCheckoutSessionsResourceWithStreamingResponse,
)

__all__ = ["BetasResource", "AsyncBetasResource"]


class BetasResource(SyncAPIResource):
    @cached_property
    def checkout_sessions(self) -> CheckoutSessionsResource:
        return CheckoutSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> BetasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return BetasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BetasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return BetasResourceWithStreamingResponse(self)


class AsyncBetasResource(AsyncAPIResource):
    @cached_property
    def checkout_sessions(self) -> AsyncCheckoutSessionsResource:
        return AsyncCheckoutSessionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBetasResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBetasResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBetasResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncBetasResourceWithStreamingResponse(self)


class BetasResourceWithRawResponse:
    def __init__(self, betas: BetasResource) -> None:
        self._betas = betas

    @cached_property
    def checkout_sessions(self) -> CheckoutSessionsResourceWithRawResponse:
        return CheckoutSessionsResourceWithRawResponse(self._betas.checkout_sessions)


class AsyncBetasResourceWithRawResponse:
    def __init__(self, betas: AsyncBetasResource) -> None:
        self._betas = betas

    @cached_property
    def checkout_sessions(self) -> AsyncCheckoutSessionsResourceWithRawResponse:
        return AsyncCheckoutSessionsResourceWithRawResponse(self._betas.checkout_sessions)


class BetasResourceWithStreamingResponse:
    def __init__(self, betas: BetasResource) -> None:
        self._betas = betas

    @cached_property
    def checkout_sessions(self) -> CheckoutSessionsResourceWithStreamingResponse:
        return CheckoutSessionsResourceWithStreamingResponse(self._betas.checkout_sessions)


class AsyncBetasResourceWithStreamingResponse:
    def __init__(self, betas: AsyncBetasResource) -> None:
        self._betas = betas

    @cached_property
    def checkout_sessions(self) -> AsyncCheckoutSessionsResourceWithStreamingResponse:
        return AsyncCheckoutSessionsResourceWithStreamingResponse(self._betas.checkout_sessions)
