# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import (
    CheckoutIntent,
)
from checkout_intents.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheckoutIntents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="productUrl",
            quantity=1,
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
                "address2": "Apt 1",
            },
            product_url="productUrl",
            quantity=1,
            constraints={
                "max_shipping_price": 500,
                "max_total_price": 100000,
                "offer_retrieval_effort": "max",
            },
            promo_codes=["sqF12lZ1VlBb"],
            variant_selections=[
                {
                    "label": "Size, Color, etc.",
                    "value": "Small, Red, XS, L, etc.",
                }
            ],
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: CheckoutIntents) -> None:
        response = client.checkout_intents.with_raw_response.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="productUrl",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: CheckoutIntents) -> None:
        with client.checkout_intents.with_streaming_response.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="productUrl",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.retrieve(
            "id",
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: CheckoutIntents) -> None:
        response = client.checkout_intents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: CheckoutIntents) -> None:
        with client.checkout_intents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_intents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.list()
        assert_matches_type(SyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.list(
            id=["string"],
            after="after",
            before="before",
            limit=0,
            state=["retrieving_offer"],
        )
        assert_matches_type(SyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: CheckoutIntents) -> None:
        response = client.checkout_intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = response.parse()
        assert_matches_type(SyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: CheckoutIntents) -> None:
        with client.checkout_intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = response.parse()
            assert_matches_type(SyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_payment(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_payment_with_all_params(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_payment(self, client: CheckoutIntents) -> None:
        response = client.checkout_intents.with_raw_response.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_payment(self, client: CheckoutIntents) -> None:
        with client.checkout_intents.with_streaming_response.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add_payment(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_intents.with_raw_response.add_payment(
                id="",
                payment_method={
                    "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                    "type": "stripe_token",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_confirm_with_all_params(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_confirm(self, client: CheckoutIntents) -> None:
        response = client.checkout_intents.with_raw_response.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_confirm(self, client: CheckoutIntents) -> None:
        with client.checkout_intents.with_streaming_response.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_confirm(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.checkout_intents.with_raw_response.confirm(
                id="",
                payment_method={
                    "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                    "type": "stripe_token",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purchase(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_purchase_with_all_params(self, client: CheckoutIntents) -> None:
        checkout_intent = client.checkout_intents.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
                "address2": "Apt 1",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
            constraints={
                "max_shipping_price": 500,
                "max_total_price": 100000,
                "offer_retrieval_effort": "max",
            },
            promo_codes=["sqF12lZ1VlBb"],
            variant_selections=[
                {
                    "label": "Size, Color, etc.",
                    "value": "Small, Red, XS, L, etc.",
                }
            ],
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_purchase(self, client: CheckoutIntents) -> None:
        response = client.checkout_intents.with_raw_response.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_purchase(self, client: CheckoutIntents) -> None:
        with client.checkout_intents.with_streaming_response.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCheckoutIntents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="productUrl",
            quantity=1,
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
                "address2": "Apt 1",
            },
            product_url="productUrl",
            quantity=1,
            constraints={
                "max_shipping_price": 500,
                "max_total_price": 100000,
                "offer_retrieval_effort": "max",
            },
            promo_codes=["sqF12lZ1VlBb"],
            variant_selections=[
                {
                    "label": "Size, Color, etc.",
                    "value": "Small, Red, XS, L, etc.",
                }
            ],
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.checkout_intents.with_raw_response.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="productUrl",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = await response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.checkout_intents.with_streaming_response.create(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="productUrl",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = await response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.retrieve(
            "id",
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.checkout_intents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = await response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.checkout_intents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = await response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_intents.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.list()
        assert_matches_type(AsyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.list(
            id=["string"],
            after="after",
            before="before",
            limit=0,
            state=["retrieving_offer"],
        )
        assert_matches_type(AsyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.checkout_intents.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = await response.parse()
        assert_matches_type(AsyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.checkout_intents.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = await response.parse()
            assert_matches_type(AsyncCursorPagination[CheckoutIntent], checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_payment(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_payment_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_payment(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.checkout_intents.with_raw_response.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = await response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_payment(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.checkout_intents.with_streaming_response.add_payment(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = await response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add_payment(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_intents.with_raw_response.add_payment(
                id="",
                payment_method={
                    "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                    "type": "stripe_token",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_confirm_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_confirm(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.checkout_intents.with_raw_response.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = await response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_confirm(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.checkout_intents.with_streaming_response.confirm(
            id="id",
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = await response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_confirm(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.checkout_intents.with_raw_response.confirm(
                id="",
                payment_method={
                    "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                    "type": "stripe_token",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purchase(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_purchase_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        checkout_intent = await async_client.checkout_intents.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
                "address2": "Apt 1",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
            constraints={
                "max_shipping_price": 500,
                "max_total_price": 100000,
                "offer_retrieval_effort": "max",
            },
            promo_codes=["sqF12lZ1VlBb"],
            variant_selections=[
                {
                    "label": "Size, Color, etc.",
                    "value": "Small, Red, XS, L, etc.",
                }
            ],
        )
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_purchase(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.checkout_intents.with_raw_response.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        checkout_intent = await response.parse()
        assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_purchase(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.checkout_intents.with_streaming_response.purchase(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "john.doe@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "1234567890",
                "postal_code": "10001",
                "province": "NY",
            },
            payment_method={
                "stripe_token": "tok_1RkrWWHGDlstla3f1Fc7ZrhH",
                "type": "stripe_token",
            },
            product_url="productUrl",
            quantity=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            checkout_intent = await response.parse()
            assert_matches_type(CheckoutIntent, checkout_intent, path=["response"])

        assert cast(Any, response.is_closed) is True
