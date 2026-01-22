# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import CheckoutSession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: CheckoutIntents) -> None:
        checkout_session = client.betas.checkout_sessions.create(
            product_url="productUrl",
            quantity=1,
        )
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: CheckoutIntents) -> None:
        checkout_session = client.betas.checkout_sessions.create(
            product_url="productUrl",
            quantity=1,
            buyer={
                "address1": "123 Main St",
                "address2": "Apt 1",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            constraints={
                "max_shipping_price": 500,
                "max_total_price": 100000,
                "offer_retrieval_effort": "max",
            },
            promo_codes=["string"],
            variant_selections=[
                {
                    "label": "Size, Color, etc.",
                    "value": "Small, Red, XS, L, etc.",
                }
            ],
        )
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: CheckoutIntents) -> None:
        response = client.betas.checkout_sessions.with_raw_response.create(
            product_url="productUrl",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = response.parse()
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: CheckoutIntents) -> None:
        with client.betas.checkout_sessions.with_streaming_response.create(
            product_url="productUrl",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = response.parse()
            assert_matches_type(CheckoutSession, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCheckoutSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_session = await async_client.betas.checkout_sessions.create(
            product_url="productUrl",
            quantity=1,
        )
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_session = await async_client.betas.checkout_sessions.create(
            product_url="productUrl",
            quantity=1,
            buyer={
                "address1": "123 Main St",
                "address2": "Apt 1",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            constraints={
                "max_shipping_price": 500,
                "max_total_price": 100000,
                "offer_retrieval_effort": "max",
            },
            promo_codes=["string"],
            variant_selections=[
                {
                    "label": "Size, Color, etc.",
                    "value": "Small, Red, XS, L, etc.",
                }
            ],
        )
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.betas.checkout_sessions.with_raw_response.create(
            product_url="productUrl",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_session = await response.parse()
        assert_matches_type(CheckoutSession, checkout_session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.betas.checkout_sessions.with_streaming_response.create(
            product_url="productUrl",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_session = await response.parse()
            assert_matches_type(CheckoutSession, checkout_session, path=["response"])

        assert cast(Any, response.is_closed) is True
