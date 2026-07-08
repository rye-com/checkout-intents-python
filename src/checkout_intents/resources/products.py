# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import product_lookup_params, product_subscribe_params, product_unsubscribe_params
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.product import Product
from ..types.product_subscription import ProductSubscription
from ..types.product_list_subscriptions_response import ProductListSubscriptionsResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def list_subscriptions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListSubscriptionsResponse:
        """Retrieve product subscription rules."""
        return self._get(
            "/api/v1/products/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListSubscriptionsResponse,
        )

    def lookup(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Lookup a product's information by URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/products/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, product_lookup_params.ProductLookupParams),
            ),
            cast_to=Product,
        )

    def subscribe(
        self,
        *,
        type: Literal["store", "product"],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProductSubscription:
        """
        Subscribe to product events for one integrated Shopify URL.

        Args:
          type: Scope of the subscription change.

          url: Store or product URL to subscribe or unsubscribe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return cast(
            ProductSubscription,
            self._post(
                "/api/v1/products/subscribe",
                body=maybe_transform(
                    {
                        "type": type,
                        "url": url,
                    },
                    product_subscribe_params.ProductSubscribeParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, ProductSubscription
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def unsubscribe(
        self,
        *,
        type: Literal["store", "product"],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProductSubscription:
        """
        Unsubscribe from product events for one integrated Shopify URL.

        Args:
          type: Scope of the subscription change.

          url: Store or product URL to subscribe or unsubscribe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return cast(
            ProductSubscription,
            self._post(
                "/api/v1/products/unsubscribe",
                body=maybe_transform(
                    {
                        "type": type,
                        "url": url,
                    },
                    product_unsubscribe_params.ProductUnsubscribeParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, ProductSubscription
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def list_subscriptions(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListSubscriptionsResponse:
        """Retrieve product subscription rules."""
        return await self._get(
            "/api/v1/products/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductListSubscriptionsResponse,
        )

    async def lookup(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Product:
        """
        Lookup a product's information by URL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/products/lookup",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, product_lookup_params.ProductLookupParams),
            ),
            cast_to=Product,
        )

    async def subscribe(
        self,
        *,
        type: Literal["store", "product"],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProductSubscription:
        """
        Subscribe to product events for one integrated Shopify URL.

        Args:
          type: Scope of the subscription change.

          url: Store or product URL to subscribe or unsubscribe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return cast(
            ProductSubscription,
            await self._post(
                "/api/v1/products/subscribe",
                body=await async_maybe_transform(
                    {
                        "type": type,
                        "url": url,
                    },
                    product_subscribe_params.ProductSubscribeParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, ProductSubscription
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def unsubscribe(
        self,
        *,
        type: Literal["store", "product"],
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        idempotency_key: str | None = None,
    ) -> ProductSubscription:
        """
        Unsubscribe from product events for one integrated Shopify URL.

        Args:
          type: Scope of the subscription change.

          url: Store or product URL to subscribe or unsubscribe.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return cast(
            ProductSubscription,
            await self._post(
                "/api/v1/products/unsubscribe",
                body=await async_maybe_transform(
                    {
                        "type": type,
                        "url": url,
                    },
                    product_unsubscribe_params.ProductUnsubscribeParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    idempotency_key=idempotency_key,
                ),
                cast_to=cast(
                    Any, ProductSubscription
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list_subscriptions = to_raw_response_wrapper(
            products.list_subscriptions,
        )
        self.lookup = to_raw_response_wrapper(
            products.lookup,
        )
        self.subscribe = to_raw_response_wrapper(
            products.subscribe,
        )
        self.unsubscribe = to_raw_response_wrapper(
            products.unsubscribe,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list_subscriptions = async_to_raw_response_wrapper(
            products.list_subscriptions,
        )
        self.lookup = async_to_raw_response_wrapper(
            products.lookup,
        )
        self.subscribe = async_to_raw_response_wrapper(
            products.subscribe,
        )
        self.unsubscribe = async_to_raw_response_wrapper(
            products.unsubscribe,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list_subscriptions = to_streamed_response_wrapper(
            products.list_subscriptions,
        )
        self.lookup = to_streamed_response_wrapper(
            products.lookup,
        )
        self.subscribe = to_streamed_response_wrapper(
            products.subscribe,
        )
        self.unsubscribe = to_streamed_response_wrapper(
            products.unsubscribe,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list_subscriptions = async_to_streamed_response_wrapper(
            products.list_subscriptions,
        )
        self.lookup = async_to_streamed_response_wrapper(
            products.lookup,
        )
        self.subscribe = async_to_streamed_response_wrapper(
            products.subscribe,
        )
        self.unsubscribe = async_to_streamed_response_wrapper(
            products.unsubscribe,
        )
