# Tests for polling helper functions

from __future__ import annotations

import logging

import httpx
import pytest
from respx import MockRouter

from checkout_intents import CheckoutIntents, AsyncCheckoutIntents
from checkout_intents._exceptions import PollTimeoutError

base_url = "http://127.0.0.1:4010"
api_key = "RYE/staging-test-key"


class TestSyncPolling:
    """Tests for synchronous polling functions"""

    @pytest.mark.respx(base_url=base_url)
    def test_poll_until_completed_success(self, respx_mock: MockRouter) -> None:
        """Test that poll_until_completed returns when state reaches completed"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        # First call returns placing_order, second returns completed
        call_count = 0

        def retrieve_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return httpx.Response(
                    200,
                    json={
                        "id": "ci_123456",
                        "buyer": {
                            "address1": "123 Main St",
                            "city": "New York",
                            "country": "US",
                            "email": "test@example.com",
                            "firstName": "John",
                            "lastName": "Doe",
                            "phone": "5555555555",
                            "postalCode": "10001",
                            "province": "NY",
                        },
                        "createdAt": "2024-01-01T00:00:00Z",
                        "productUrl": "https://example.com/product",
                        "quantity": 1,
                        "state": "placing_order",
                        "offer": {
                            "cost": {
                                "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                                "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                            },
                            "shipping": {"availableOptions": []},
                        },
                        "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                    },
                )
            return httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "completed",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(side_effect=retrieve_handler)

        # Poll with very short interval for testing
        result = client.checkout_intents.poll_until_completed("ci_123456", poll_interval=0.01, max_attempts=10)

        assert result.state == "completed"
        assert call_count == 2
        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_poll_until_completed_failed_state(self, respx_mock: MockRouter) -> None:
        """Test that poll_until_completed returns when state reaches failed"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "failed",
                    "failureReason": {"code": "payment_failed", "message": "Payment failed"},
                },
            )
        )

        result = client.checkout_intents.poll_until_completed("ci_123456", poll_interval=0.01)

        assert result.state == "failed"
        assert result.failure_reason.code == "payment_failed"
        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_poll_until_completed_timeout(self, respx_mock: MockRouter) -> None:
        """Test that poll_until_completed times out after max_attempts"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        # Always return placing_order to trigger timeout
        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "placing_order",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )
        )

        with pytest.raises(PollTimeoutError, match="Polling timeout") as exc_info:
            client.checkout_intents.poll_until_completed("ci_123456", poll_interval=0.01, max_attempts=2)

        # Verify error attributes
        error = exc_info.value
        assert error.intent_id == "ci_123456"
        assert error.attempts == 2
        assert error.poll_interval == 0.01
        assert error.max_attempts == 2
        assert "ci_123456" in str(error)
        assert "2 attempts" in str(error)

        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_poll_until_awaiting_confirmation(self, respx_mock: MockRouter) -> None:
        """Test that poll_until_awaiting_confirmation returns when state reaches awaiting_confirmation"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "awaiting_confirmation",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                },
            )
        )

        result = client.checkout_intents.poll_until_awaiting_confirmation("ci_123456", poll_interval=0.01)

        assert result.state == "awaiting_confirmation"
        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_create_and_poll(self, respx_mock: MockRouter) -> None:
        """Test that create_and_poll creates and then polls"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        # Mock create response
        respx_mock.post("/api/v1/checkout-intents").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "retrieving_offer",
                },
            )
        )

        # Mock retrieve response (after polling)
        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "awaiting_confirmation",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                },
            )
        )

        result = client.checkout_intents.create_and_poll(
            buyer={
                "address1": "123 Main St",
                "city": "New York",
                "country": "US",
                "email": "test@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "5555555555",
                "postal_code": "10001",
                "province": "NY",
            },
            product_url="https://example.com/product",
            quantity=1,
            poll_interval=0.01,
        )

        assert result.state == "awaiting_confirmation"
        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_confirm_and_poll(self, respx_mock: MockRouter) -> None:
        """Test that confirm_and_poll confirms and then polls"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        # Mock confirm response
        respx_mock.post("/api/v1/checkout-intents/ci_123456/confirm").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "placing_order",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )
        )

        # Mock retrieve response (after polling)
        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "completed",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )
        )

        result = client.checkout_intents.confirm_and_poll(
            "ci_123456",
            payment_method={"type": "stripe_token", "stripe_token": "tok_test"},
            poll_interval=0.01,
        )

        assert result.state == "completed"
        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_server_retry_after_header(self, respx_mock: MockRouter) -> None:
        """Test that polling respects the retry-after-ms header from server"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        call_count = 0
        sleep_times: list[float] = []

        # Mock _sleep to capture sleep times
        _original_sleep = client.checkout_intents._sleep

        def mock_sleep(seconds: float) -> None:
            sleep_times.append(seconds)
            # Don't actually sleep in tests
            pass

        client.checkout_intents._sleep = mock_sleep  # type: ignore[method-assign]

        def retrieve_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                # First response suggests retry after 1 second (1000ms)
                return httpx.Response(
                    200,
                    json={
                        "id": "ci_123456",
                        "buyer": {
                            "address1": "123 Main St",
                            "city": "New York",
                            "country": "US",
                            "email": "test@example.com",
                            "firstName": "John",
                            "lastName": "Doe",
                            "phone": "5555555555",
                            "postalCode": "10001",
                            "province": "NY",
                        },
                        "createdAt": "2024-01-01T00:00:00Z",
                        "productUrl": "https://example.com/product",
                        "quantity": 1,
                        "state": "placing_order",
                        "offer": {
                            "cost": {
                                "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                                "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                            },
                            "shipping": {"availableOptions": []},
                        },
                        "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                    },
                    headers={"retry-after-ms": "1000"},
                )
            return httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "completed",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(side_effect=retrieve_handler)

        result = client.checkout_intents.poll_until_completed("ci_123456", poll_interval=0.1, max_attempts=10)

        assert result.state == "completed"
        # Should have used the server-suggested interval (1 second = 1.0)
        assert len(sleep_times) == 1
        assert sleep_times[0] == 1.0

        client.close()

    @pytest.mark.respx(base_url=base_url)
    def test_poll_until_completed_coerces_max_attempts_less_than_1(
        self, respx_mock: MockRouter, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test that poll_until_completed coerces max_attempts < 1 to 1 and logs warning"""
        client = CheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        call_count = 0

        def retrieve_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            return httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "completed",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(side_effect=retrieve_handler)

        # Test with max_attempts = 0
        with caplog.at_level(logging.WARNING):
            result = client.checkout_intents.poll_until_completed(
                "ci_123456",
                poll_interval=0.01,
                max_attempts=0,
            )

        assert result.state == "completed"
        # Should have been called exactly once (coerced to 1)
        assert call_count == 1
        # Should have logged a warning
        assert any(
            "[Checkout Intents SDK] Invalid max_attempts value: 0" in record.message for record in caplog.records
        )

        client.close()


class TestAsyncPolling:
    """Tests for asynchronous polling functions"""

    @pytest.mark.respx(base_url=base_url)
    async def test_poll_until_completed_success(self, respx_mock: MockRouter) -> None:
        """Test that async poll_until_completed returns when state reaches completed"""
        client = AsyncCheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "completed",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )
        )

        result = await client.checkout_intents.poll_until_completed("ci_123456", poll_interval=0.01)

        assert result.state == "completed"
        await client.close()

    @pytest.mark.respx(base_url=base_url)
    async def test_poll_until_awaiting_confirmation(self, respx_mock: MockRouter) -> None:
        """Test that async poll_until_awaiting_confirmation works"""
        client = AsyncCheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(
            return_value=httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "awaiting_confirmation",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                },
            )
        )

        result = await client.checkout_intents.poll_until_awaiting_confirmation("ci_123456", poll_interval=0.01)

        assert result.state == "awaiting_confirmation"
        await client.close()

    @pytest.mark.respx(base_url=base_url)
    async def test_poll_until_completed_coerces_max_attempts_less_than_1(
        self, respx_mock: MockRouter, caplog: pytest.LogCaptureFixture
    ) -> None:
        """Test that async poll_until_completed coerces max_attempts < 1 to 1 and logs warning"""
        client = AsyncCheckoutIntents(base_url=base_url, api_key=api_key, _strict_response_validation=True)

        call_count = 0

        def retrieve_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal call_count
            call_count += 1
            return httpx.Response(
                200,
                json={
                    "id": "ci_123456",
                    "buyer": {
                        "address1": "123 Main St",
                        "city": "New York",
                        "country": "US",
                        "email": "test@example.com",
                        "firstName": "John",
                        "lastName": "Doe",
                        "phone": "5555555555",
                        "postalCode": "10001",
                        "province": "NY",
                    },
                    "createdAt": "2024-01-01T00:00:00Z",
                    "productUrl": "https://example.com/product",
                    "quantity": 1,
                    "state": "completed",
                    "offer": {
                        "cost": {
                            "subtotal": {"amountSubunits": 1000, "currencyCode": "USD"},
                            "total": {"amountSubunits": 1100, "currencyCode": "USD"},
                        },
                        "shipping": {"availableOptions": []},
                    },
                    "paymentMethod": {"type": "stripe_token", "stripeToken": "tok_test"},
                },
            )

        respx_mock.get("/api/v1/checkout-intents/ci_123456").mock(side_effect=retrieve_handler)

        # Test with max_attempts = 0
        with caplog.at_level(logging.WARNING):
            result = await client.checkout_intents.poll_until_completed(
                "ci_123456",
                poll_interval=0.01,
                max_attempts=0,
            )

        assert result.state == "completed"
        # Should have been called exactly once (coerced to 1)
        assert call_count == 1
        # Should have logged a warning
        assert any(
            "[Checkout Intents SDK] Invalid max_attempts value: 0" in record.message for record in caplog.records
        )

        await client.close()
