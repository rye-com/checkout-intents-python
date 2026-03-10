# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import Shipment
from checkout_intents.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShipments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: CheckoutIntents) -> None:
        shipment = client.shipments.retrieve(
            "id",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: CheckoutIntents) -> None:
        response = client.shipments.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: CheckoutIntents) -> None:
        with client.shipments.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.shipments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: CheckoutIntents) -> None:
        shipment = client.shipments.list()
        assert_matches_type(SyncCursorPagination[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: CheckoutIntents) -> None:
        shipment = client.shipments.list(
            after="after",
            before="before",
            ids=["string"],
            limit=1,
            status=["out_for_delivery"],
        )
        assert_matches_type(SyncCursorPagination[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: CheckoutIntents) -> None:
        response = client.shipments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = response.parse()
        assert_matches_type(SyncCursorPagination[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: CheckoutIntents) -> None:
        with client.shipments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = response.parse()
            assert_matches_type(SyncCursorPagination[Shipment], shipment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShipments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        shipment = await async_client.shipments.retrieve(
            "id",
        )
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.shipments.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(Shipment, shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.shipments.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(Shipment, shipment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.shipments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCheckoutIntents) -> None:
        shipment = await async_client.shipments.list()
        assert_matches_type(AsyncCursorPagination[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        shipment = await async_client.shipments.list(
            after="after",
            before="before",
            ids=["string"],
            limit=1,
            status=["out_for_delivery"],
        )
        assert_matches_type(AsyncCursorPagination[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.shipments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shipment = await response.parse()
        assert_matches_type(AsyncCursorPagination[Shipment], shipment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.shipments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shipment = await response.parse()
            assert_matches_type(AsyncCursorPagination[Shipment], shipment, path=["response"])

        assert cast(Any, response.is_closed) is True
