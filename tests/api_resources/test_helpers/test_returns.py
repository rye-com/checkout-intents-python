# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents.types import Return

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReturns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.create(
            order_id="orderId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.create(
            order_id="orderId",
            line_items=[
                {
                    "order_line_item_id": "orderLineItemId",
                    "quantity": 1,
                }
            ],
            reason="defective",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: CheckoutIntents) -> None:
        response = client.test_helpers.returns.with_raw_response.create(
            order_id="orderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: CheckoutIntents) -> None:
        with client.test_helpers.returns.with_streaming_response.create(
            order_id="orderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.approve(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_approve_with_all_params(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.approve(
            return_id="returnId",
            next_action="ship_items_to_merchant",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_approve(self, client: CheckoutIntents) -> None:
        response = client.test_helpers.returns.with_raw_response.approve(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_approve(self, client: CheckoutIntents) -> None:
        with client.test_helpers.returns.with_streaming_response.approve(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_approve(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            client.test_helpers.returns.with_raw_response.approve(
                return_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deny(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.deny(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_deny_with_all_params(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.deny(
            return_id="returnId",
            note="note",
            reason="final_sale",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_deny(self, client: CheckoutIntents) -> None:
        response = client.test_helpers.returns.with_raw_response.deny(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_deny(self, client: CheckoutIntents) -> None:
        with client.test_helpers.returns.with_streaming_response.deny(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_deny(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            client.test_helpers.returns.with_raw_response.deny(
                return_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fail(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.fail(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fail_with_all_params(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.fail(
            return_id="returnId",
            note="note",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fail(self, client: CheckoutIntents) -> None:
        response = client.test_helpers.returns.with_raw_response.fail(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fail(self, client: CheckoutIntents) -> None:
        with client.test_helpers.returns.with_streaming_response.fail(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_fail(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            client.test_helpers.returns.with_raw_response.fail(
                return_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refund(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.refund(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_refund_with_all_params(self, client: CheckoutIntents) -> None:
        return_ = client.test_helpers.returns.refund(
            return_id="returnId",
            cost_bearer="shopper",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_refund(self, client: CheckoutIntents) -> None:
        response = client.test_helpers.returns.with_raw_response.refund(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_refund(self, client: CheckoutIntents) -> None:
        with client.test_helpers.returns.with_streaming_response.refund(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_refund(self, client: CheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            client.test_helpers.returns.with_raw_response.refund(
                return_id="",
            )


class TestAsyncReturns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.create(
            order_id="orderId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.create(
            order_id="orderId",
            line_items=[
                {
                    "order_line_item_id": "orderLineItemId",
                    "quantity": 1,
                }
            ],
            reason="defective",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.test_helpers.returns.with_raw_response.create(
            order_id="orderId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = await response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.test_helpers.returns.with_streaming_response.create(
            order_id="orderId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.approve(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_approve_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.approve(
            return_id="returnId",
            next_action="ship_items_to_merchant",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.test_helpers.returns.with_raw_response.approve(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = await response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.test_helpers.returns.with_streaming_response.approve(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_approve(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            await async_client.test_helpers.returns.with_raw_response.approve(
                return_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deny(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.deny(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_deny_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.deny(
            return_id="returnId",
            note="note",
            reason="final_sale",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_deny(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.test_helpers.returns.with_raw_response.deny(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = await response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_deny(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.test_helpers.returns.with_streaming_response.deny(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_deny(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            await async_client.test_helpers.returns.with_raw_response.deny(
                return_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fail(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.fail(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fail_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.fail(
            return_id="returnId",
            note="note",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fail(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.test_helpers.returns.with_raw_response.fail(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = await response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fail(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.test_helpers.returns.with_streaming_response.fail(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_fail(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            await async_client.test_helpers.returns.with_raw_response.fail(
                return_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refund(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.refund(
            return_id="returnId",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_refund_with_all_params(self, async_client: AsyncCheckoutIntents) -> None:
        return_ = await async_client.test_helpers.returns.refund(
            return_id="returnId",
            cost_bearer="shopper",
        )
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_refund(self, async_client: AsyncCheckoutIntents) -> None:
        response = await async_client.test_helpers.returns.with_raw_response.refund(
            return_id="returnId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        return_ = await response.parse()
        assert_matches_type(Return, return_, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_refund(self, async_client: AsyncCheckoutIntents) -> None:
        async with async_client.test_helpers.returns.with_streaming_response.refund(
            return_id="returnId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            return_ = await response.parse()
            assert_matches_type(Return, return_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_refund(self, async_client: AsyncCheckoutIntents) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `return_id` but received ''"):
            await async_client.test_helpers.returns.with_raw_response.refund(
                return_id="",
            )
