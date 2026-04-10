# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import (
    BillingGetBalanceResponse,
    BillingListTransactionsResponse,
    BillingCreateTopupInvoiceResponse,
)
from checkout_intents.pagination import SyncCursorPagination, AsyncCursorPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_topup_invoice(self, client: CheckoutIntents) -> None:
        billing = client.billing.cancel_topup_invoice(
            "invoiceId",
        )
        assert billing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_topup_invoice(self, client: CheckoutIntents) -> None:
        response = client.billing.with_raw_response.cancel_topup_invoice(
            "invoiceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert billing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_topup_invoice(self, client: CheckoutIntents) -> None:
        with client.billing.with_streaming_response.cancel_topup_invoice(
            "invoiceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert billing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel_topup_invoice(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            client.billing.with_raw_response.cancel_topup_invoice(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_topup_invoice(self, client: CheckoutIntents) -> None:
        billing = client.billing.create_topup_invoice(
            amount_subunits=500000,
        )
        assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_topup_invoice_with_all_params(self, client: CheckoutIntents) -> None:
        billing = client.billing.create_topup_invoice(
            amount_subunits=500000,
            charge_automatically=False,
        )
        assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_topup_invoice(self, client: CheckoutIntents) -> None:
        response = client.billing.with_raw_response.create_topup_invoice(
            amount_subunits=500000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_topup_invoice(self, client: CheckoutIntents) -> None:
        with client.billing.with_streaming_response.create_topup_invoice(
            amount_subunits=500000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_balance(self, client: CheckoutIntents) -> None:
        billing = client.billing.get_balance()
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_balance(self, client: CheckoutIntents) -> None:
        response = client.billing.with_raw_response.get_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_balance(self, client: CheckoutIntents) -> None:
        with client.billing.with_streaming_response.get_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: CheckoutIntents) -> None:
        billing = client.billing.list_transactions()
        assert_matches_type(SyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: CheckoutIntents) -> None:
        billing = client.billing.list_transactions(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(SyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: CheckoutIntents) -> None:
        response = client.billing.with_raw_response.list_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(SyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: CheckoutIntents) -> None:
        with client.billing.with_streaming_response.list_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(SyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        billing = await async_client.billing.cancel_topup_invoice(
            "invoiceId",
        )
        assert billing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.billing.with_raw_response.cancel_topup_invoice(
            "invoiceId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert billing is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.billing.with_streaming_response.cancel_topup_invoice(
            "invoiceId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert billing is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `invoice_id` but received ''"):
            await async_client.billing.with_raw_response.cancel_topup_invoice(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        billing = await async_client.billing.create_topup_invoice(
            amount_subunits=500000,
        )
        assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_topup_invoice_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        billing = await async_client.billing.create_topup_invoice(
            amount_subunits=500000,
            charge_automatically=False,
        )
        assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.billing.with_raw_response.create_topup_invoice(
            amount_subunits=500000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_topup_invoice(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.billing.with_streaming_response.create_topup_invoice(
            amount_subunits=500000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingCreateTopupInvoiceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_balance(self, async_client: AsyncCheckoutIntents) -> None:
        billing = await async_client.billing.get_balance()
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_balance(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.billing.with_raw_response.get_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_balance(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.billing.with_streaming_response.get_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetBalanceResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncCheckoutIntents) -> None:
        billing = await async_client.billing.list_transactions()
        assert_matches_type(AsyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        billing = await async_client.billing.list_transactions(
            after="after",
            before="before",
            limit=1,
        )
        assert_matches_type(AsyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.billing.with_raw_response.list_transactions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(AsyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.billing.with_streaming_response.list_transactions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(AsyncCursorPagination[BillingListTransactionsResponse], billing, path=["response"])

        assert cast(Any, response.is_closed) is True
