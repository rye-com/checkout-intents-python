# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import merchant_connector_create_installation_link_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.installation_link import InstallationLink

__all__ = ["MerchantConnectorsResource", "AsyncMerchantConnectorsResource"]


class MerchantConnectorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MerchantConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return MerchantConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MerchantConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return MerchantConnectorsResourceWithStreamingResponse(self)

    def create_installation_link(
        self,
        connector: Literal["shopify"],
        *,
        store_url: str,
        private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationLink:
        """Generate an installation link for a merchant connector (e.g.

        Shopify).

        The returned URL begins the connector's OAuth handshake. Direct the merchant to
        it; once they authorize the Rye app, the connector redirects back to Rye to
        complete the install. The merchant is attributed to the calling developer and
        becomes available for checkout via this account.

        Args:
          connector: A merchant connector is a Rye integration with a third-party merchant platform
              (e.g. Shopify) that lets developers onboard merchants to Rye. Today only Shopify
              is supported; this union expands as we add support for additional connectors
              (Woocommerce, BigCommerce, etc.).

          store_url: Domain or URL of the merchant store to generate the installation link for

          private: If true, the merchant onboarded via this link is exclusive to the calling
              developer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector:
            raise ValueError(f"Expected a non-empty value for `connector` but received {connector!r}")
        return self._get(
            path_template("/api/v1/merchant-connectors/{connector}/installation-link", connector=connector),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "store_url": store_url,
                        "private": private,
                    },
                    merchant_connector_create_installation_link_params.MerchantConnectorCreateInstallationLinkParams,
                ),
            ),
            cast_to=InstallationLink,
        )


class AsyncMerchantConnectorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMerchantConnectorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMerchantConnectorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMerchantConnectorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncMerchantConnectorsResourceWithStreamingResponse(self)

    async def create_installation_link(
        self,
        connector: Literal["shopify"],
        *,
        store_url: str,
        private: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallationLink:
        """Generate an installation link for a merchant connector (e.g.

        Shopify).

        The returned URL begins the connector's OAuth handshake. Direct the merchant to
        it; once they authorize the Rye app, the connector redirects back to Rye to
        complete the install. The merchant is attributed to the calling developer and
        becomes available for checkout via this account.

        Args:
          connector: A merchant connector is a Rye integration with a third-party merchant platform
              (e.g. Shopify) that lets developers onboard merchants to Rye. Today only Shopify
              is supported; this union expands as we add support for additional connectors
              (Woocommerce, BigCommerce, etc.).

          store_url: Domain or URL of the merchant store to generate the installation link for

          private: If true, the merchant onboarded via this link is exclusive to the calling
              developer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not connector:
            raise ValueError(f"Expected a non-empty value for `connector` but received {connector!r}")
        return await self._get(
            path_template("/api/v1/merchant-connectors/{connector}/installation-link", connector=connector),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "store_url": store_url,
                        "private": private,
                    },
                    merchant_connector_create_installation_link_params.MerchantConnectorCreateInstallationLinkParams,
                ),
            ),
            cast_to=InstallationLink,
        )


class MerchantConnectorsResourceWithRawResponse:
    def __init__(self, merchant_connectors: MerchantConnectorsResource) -> None:
        self._merchant_connectors = merchant_connectors

        self.create_installation_link = to_raw_response_wrapper(
            merchant_connectors.create_installation_link,
        )


class AsyncMerchantConnectorsResourceWithRawResponse:
    def __init__(self, merchant_connectors: AsyncMerchantConnectorsResource) -> None:
        self._merchant_connectors = merchant_connectors

        self.create_installation_link = async_to_raw_response_wrapper(
            merchant_connectors.create_installation_link,
        )


class MerchantConnectorsResourceWithStreamingResponse:
    def __init__(self, merchant_connectors: MerchantConnectorsResource) -> None:
        self._merchant_connectors = merchant_connectors

        self.create_installation_link = to_streamed_response_wrapper(
            merchant_connectors.create_installation_link,
        )


class AsyncMerchantConnectorsResourceWithStreamingResponse:
    def __init__(self, merchant_connectors: AsyncMerchantConnectorsResource) -> None:
        self._merchant_connectors = merchant_connectors

        self.create_installation_link = async_to_streamed_response_wrapper(
            merchant_connectors.create_installation_link,
        )
