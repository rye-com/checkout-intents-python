# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import Commission
from checkout_intents.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCommissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: CheckoutIntents) -> None:
        commission = client.commissions.list()
        assert_matches_type(SyncCursorPagination[Commission], commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: CheckoutIntents) -> None:
        commission = client.commissions.list(
            after="after",
            before="before",
            checkout_intent_id="checkoutIntentId",
            limit=1,
            status="pending",
            type="surcharge",
        )
        assert_matches_type(SyncCursorPagination[Commission], commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: CheckoutIntents) -> None:
        response = client.commissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commission = response.parse()
        assert_matches_type(SyncCursorPagination[Commission], commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: CheckoutIntents) -> None:
        with client.commissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commission = response.parse()
            assert_matches_type(SyncCursorPagination[Commission], commission, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCommissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCheckoutIntents) -> None:
        commission = await async_client.commissions.list()
        assert_matches_type(AsyncCursorPagination[Commission], commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        commission = await async_client.commissions.list(
            after="after",
            before="before",
            checkout_intent_id="checkoutIntentId",
            limit=1,
            status="pending",
            type="surcharge",
        )
        assert_matches_type(AsyncCursorPagination[Commission], commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.commissions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        commission = await response.parse()
        assert_matches_type(AsyncCursorPagination[Commission], commission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.commissions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            commission = await response.parse()
            assert_matches_type(AsyncCursorPagination[Commission], commission, path=["response"])

        assert cast(Any, response.is_closed) is True
