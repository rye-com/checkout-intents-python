# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import (
    Order,
    Cancellation,
)
from checkout_intents.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: CheckoutIntents) -> None:
        order = client.orders.retrieve(
            "id",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: CheckoutIntents) -> None:
        response = client.orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: CheckoutIntents) -> None:
        with client.orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: CheckoutIntents) -> None:
        order = client.orders.list()
        assert_matches_type(SyncCursorPagination[Order], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: CheckoutIntents) -> None:
        order = client.orders.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorPagination[Order], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: CheckoutIntents) -> None:
        response = client.orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(SyncCursorPagination[Order], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: CheckoutIntents) -> None:
        with client.orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(SyncCursorPagination[Order], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: CheckoutIntents) -> None:
        order = client.orders.cancel(
            id="id",
            reason={"code": "requested_by_customer"},
        )
        assert_matches_type(Cancellation, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: CheckoutIntents) -> None:
        order = client.orders.cancel(
            id="id",
            reason={
                "code": "requested_by_customer",
                "message": "message",
            },
        )
        assert_matches_type(Cancellation, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: CheckoutIntents) -> None:
        response = client.orders.with_raw_response.cancel(
            id="id",
            reason={"code": "requested_by_customer"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Cancellation, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: CheckoutIntents) -> None:
        with client.orders.with_streaming_response.cancel(
            id="id",
            reason={"code": "requested_by_customer"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Cancellation, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orders.with_raw_response.cancel(
                id="",
                reason={"code": "requested_by_customer"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_buyer(self, client: CheckoutIntents) -> None:
        order = client.orders.update_buyer(
            id="id",
            buyer={},
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_buyer_with_all_params(self, client: CheckoutIntents) -> None:
        order = client.orders.update_buyer(
            id="id",
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
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_buyer(self, client: CheckoutIntents) -> None:
        response = client.orders.with_raw_response.update_buyer(
            id="id",
            buyer={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_buyer(self, client: CheckoutIntents) -> None:
        with client.orders.with_streaming_response.update_buyer(
            id="id",
            buyer={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_buyer(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.orders.with_raw_response.update_buyer(
                id="",
                buyer={},
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.retrieve(
            "id",
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.orders.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.orders.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orders.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.list()
        assert_matches_type(AsyncCursorPagination[Order], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.list(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorPagination[Order], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(AsyncCursorPagination[Order], order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(AsyncCursorPagination[Order], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.cancel(
            id="id",
            reason={"code": "requested_by_customer"},
        )
        assert_matches_type(Cancellation, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.cancel(
            id="id",
            reason={
                "code": "requested_by_customer",
                "message": "message",
            },
        )
        assert_matches_type(Cancellation, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.orders.with_raw_response.cancel(
            id="id",
            reason={"code": "requested_by_customer"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Cancellation, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.orders.with_streaming_response.cancel(
            id="id",
            reason={"code": "requested_by_customer"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Cancellation, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orders.with_raw_response.cancel(
                id="",
                reason={"code": "requested_by_customer"},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_buyer(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.update_buyer(
            id="id",
            buyer={},
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_buyer_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        order = await async_client.orders.update_buyer(
            id="id",
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
        )
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_buyer(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.orders.with_raw_response.update_buyer(
            id="id",
            buyer={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Order, order, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_buyer(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.orders.with_streaming_response.update_buyer(
            id="id",
            buyer={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Order, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_buyer(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.orders.with_raw_response.update_buyer(
                id="",
                buyer={},
            )
