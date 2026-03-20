# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, cast

import httpx

from ..types import shipment_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform
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
from ..types.shipment import Shipment
from ..types.shipment_status import ShipmentStatus

__all__ = ["ShipmentsResource", "AsyncShipmentsResource"]


class ShipmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShipmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return ShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShipmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return ShipmentsResourceWithStreamingResponse(self)

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
    ) -> Shipment:
        """
        Retrieve a shipment by id

        Returns shipment information if the lookup succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Shipment,
            self._get(
                path_template("/api/v1/shipments/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Shipment),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        status: List[ShipmentStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPagination[Shipment]:
        """
        Retrieve a paginated list of shipments

        Enables developers to query shipments associated with their account, with
        filters and cursor-based pagination.

        Args:
          limit: Maximum number of results to return (default 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/shipments",
            page=SyncCursorPagination[Shipment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "ids": ids,
                        "limit": limit,
                        "status": status,
                    },
                    shipment_list_params.ShipmentListParams,
                ),
            ),
            model=cast(Any, Shipment),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncShipmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShipmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShipmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShipmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rye-com/checkout-intents-python#with_streaming_response
        """
        return AsyncShipmentsResourceWithStreamingResponse(self)

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
    ) -> Shipment:
        """
        Retrieve a shipment by id

        Returns shipment information if the lookup succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            Shipment,
            await self._get(
                path_template("/api/v1/shipments/{id}", id=id),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, Shipment),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        after: str | Omit = omit,
        before: str | Omit = omit,
        ids: SequenceNotStr[str] | Omit = omit,
        limit: int | Omit = omit,
        status: List[ShipmentStatus] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Shipment, AsyncCursorPagination[Shipment]]:
        """
        Retrieve a paginated list of shipments

        Enables developers to query shipments associated with their account, with
        filters and cursor-based pagination.

        Args:
          limit: Maximum number of results to return (default 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/shipments",
            page=AsyncCursorPagination[Shipment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "ids": ids,
                        "limit": limit,
                        "status": status,
                    },
                    shipment_list_params.ShipmentListParams,
                ),
            ),
            model=cast(Any, Shipment),  # Union types cannot be passed in as arguments in the type system
        )


class ShipmentsResourceWithRawResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.retrieve = to_raw_response_wrapper(
            shipments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            shipments.list,
        )


class AsyncShipmentsResourceWithRawResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.retrieve = async_to_raw_response_wrapper(
            shipments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            shipments.list,
        )


class ShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: ShipmentsResource) -> None:
        self._shipments = shipments

        self.retrieve = to_streamed_response_wrapper(
            shipments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            shipments.list,
        )


class AsyncShipmentsResourceWithStreamingResponse:
    def __init__(self, shipments: AsyncShipmentsResource) -> None:
        self._shipments = shipments

        self.retrieve = async_to_streamed_response_wrapper(
            shipments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            shipments.list,
        )
