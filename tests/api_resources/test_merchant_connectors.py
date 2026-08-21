# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import InstallationLink

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMerchantConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_installation_link(self, client: CheckoutIntents) -> None:
        merchant_connector = client.merchant_connectors.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
        )
        assert_matches_type(InstallationLink, merchant_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_installation_link_with_all_params(self, client: CheckoutIntents) -> None:
        merchant_connector = client.merchant_connectors.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
            private=True,
        )
        assert_matches_type(InstallationLink, merchant_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_installation_link(self, client: CheckoutIntents) -> None:
        response = client.merchant_connectors.with_raw_response.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merchant_connector = response.parse()
        assert_matches_type(InstallationLink, merchant_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_installation_link(self, client: CheckoutIntents) -> None:
        with client.merchant_connectors.with_streaming_response.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merchant_connector = response.parse()
            assert_matches_type(InstallationLink, merchant_connector, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMerchantConnectors:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_installation_link(self, async_client: AsyncCheckoutIntents) -> None:
        merchant_connector = await async_client.merchant_connectors.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
        )
        assert_matches_type(InstallationLink, merchant_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_installation_link_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        merchant_connector = await async_client.merchant_connectors.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
            private=True,
        )
        assert_matches_type(InstallationLink, merchant_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_installation_link(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.merchant_connectors.with_raw_response.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        merchant_connector = await response.parse()
        assert_matches_type(InstallationLink, merchant_connector, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_installation_link(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.merchant_connectors.with_streaming_response.create_installation_link(
            connector="shopify",
            store_url="storeUrl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            merchant_connector = await response.parse()
            assert_matches_type(InstallationLink, merchant_connector, path=["response"])

        assert cast(Any, response.is_closed) is True
