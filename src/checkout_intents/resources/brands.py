# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.brand_retrieve_response import BrandRetrieveResponse

__all__ = ["BrandsResource", "AsyncBrandsResource"]


class BrandsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return BrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return BrandsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        domain: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Retrieve brand information by domain name

        Look up a brand by its domain name (e.g. "aloyoga.com" or "www.amazon.com").
        Returns brand information including the marketplace type if the lookup succeeds.

        Args:
          domain: Represents a valid domain name string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return self._get(
            f"/api/v1/brands/domain/{domain}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )


class AsyncBrandsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncBrandsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        domain: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Retrieve brand information by domain name

        Look up a brand by its domain name (e.g. "aloyoga.com" or "www.amazon.com").
        Returns brand information including the marketplace type if the lookup succeeds.

        Args:
          domain: Represents a valid domain name string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not domain:
            raise ValueError(f"Expected a non-empty value for `domain` but received {domain!r}")
        return await self._get(
            f"/api/v1/brands/domain/{domain}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )


class BrandsResourceWithRawResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.retrieve = to_raw_response_wrapper(
            brands.retrieve,
        )


class AsyncBrandsResourceWithRawResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.retrieve = async_to_raw_response_wrapper(
            brands.retrieve,
        )


class BrandsResourceWithStreamingResponse:
    def __init__(self, brands: BrandsResource) -> None:
        self._brands = brands

        self.retrieve = to_streamed_response_wrapper(
            brands.retrieve,
        )


class AsyncBrandsResourceWithStreamingResponse:
    def __init__(self, brands: AsyncBrandsResource) -> None:
        self._brands = brands

        self.retrieve = async_to_streamed_response_wrapper(
            brands.retrieve,
        )
