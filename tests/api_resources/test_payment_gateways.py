# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import PaymentGatewaySession

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPaymentGateways:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_session(self, client: CheckoutIntents) -> None:
        payment_gateway = client.payment_gateways.create_session(
            "basis-theory",
        )
        assert_matches_type(PaymentGatewaySession, payment_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_session(self, client: CheckoutIntents) -> None:
        response = client.payment_gateways.with_raw_response.create_session(
            "basis-theory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway = response.parse()
        assert_matches_type(PaymentGatewaySession, payment_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_session(self, client: CheckoutIntents) -> None:
        with client.payment_gateways.with_streaming_response.create_session(
            "basis-theory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway = response.parse()
            assert_matches_type(PaymentGatewaySession, payment_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPaymentGateways:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_session(self, async_client: AsyncCheckoutIntents) -> None:
        payment_gateway = await async_client.payment_gateways.create_session(
            "basis-theory",
        )
        assert_matches_type(PaymentGatewaySession, payment_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_session(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.payment_gateways.with_raw_response.create_session(
            "basis-theory",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment_gateway = await response.parse()
        assert_matches_type(PaymentGatewaySession, payment_gateway, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_session(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.payment_gateways.with_streaming_response.create_session(
            "basis-theory",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment_gateway = await response.parse()
            assert_matches_type(PaymentGatewaySession, payment_gateway, path=["response"])

        assert cast(Any, response.is_closed) is True
